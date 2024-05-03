import duckdb
import pandas as pd
import numpy as np

con = duckdb.connect("../data/clean/oa_data.db")

df_annots = pd.read_csv("../data/raw/researchers.tsv", sep="\t", usecols=['oa_display_name', 'has_research_group', 'OpenAlex id'])
df_annots['pub_year'] = 2023

df_annots.value_counts('has_research_group')

df = con.sql("""
    SELECT c.target, c.all_times_collabo, c.yearly_collabo, 
        c.title as coauthor_name, a.author_age as coauthor_age, a2.author_age,
        (a2.author_age-a.author_age) AS age_diff, c.pub_year
    FROM coauthor c
    LEFT JOIN author_tidy a
    ON c.aid = a.aid AND c.pub_year = a.pub_year
    LEFT JOIN author_tidy a2
    ON c.target = a2.display_name AND c.pub_year = a2.pub_year
    WHERE c.pub_year = 2023
""").fetchdf()

df_pap = con.sql("""
    SELECT p.pub_year, p.target
    FROM paper p
    LEFT JOIN author_tidy a
    ON p.aid = a.aid AND p.pub_year = a.pub_year
    WHERE p.pub_year = 2023
""").fetchdf()


df = df[~df.age_diff.isna()]

df = df.merge(df_annots, how="inner", left_on=['target', 'pub_year'], right_on=['oa_display_name', 'pub_year'])

agg_diff_vec = df.age_diff.to_numpy()

# Create an empty array of the same shape to store the results
categories = np.empty(agg_diff_vec.shape, dtype=object)

# Apply conditions
categories[agg_diff_vec < -15] = "much_younger"
categories[(agg_diff_vec >= -15) & (agg_diff_vec < -7)] = "younger"
categories[(agg_diff_vec >= -7) & (agg_diff_vec < 7)] = "same_age"
categories[(agg_diff_vec >= 7) & (agg_diff_vec < 15)] = "older"
categories[agg_diff_vec >= 15] = "much_older"

df['age_bucket'] = categories

counts = df.groupby(['target', 'age_bucket']).size().reset_index(name='counts')
df_wide = counts.pivot(index='target', columns='age_bucket', values='counts').fillna(0).reset_index()

counts_pap = df.groupby(['target']).size().reset_index(name='nb_papers')

df_wide = df_wide.merge(counts_pap, how="left", on=['target'])
