import duckdb
import pandas as pd
import numpy as np
import argparse
from pathlib import Path

def parse_args():
    parser = argparse.ArgumentParser("Data Downloader")
    parser.add_argument(
        "-i",
        "--input",
        type= Path,
        help="JSONlines file with urls and hashes",
        required=True,
    )
    parser.add_argument(
        "-a",
        "--annots",
        type= Path,
        help="JSONlines file with urls and hashes",
        required=True,
    )
    parser.add_argument(
        "-o", "--output", type=Path, help="output directory", required=True
    )
    return parser.parse_args()

def main():
    args = parse_args()
    
    con = duckdb.connect(args.input / "oa_data.db")
    
    # Preprocess coauthor data

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

    df = df[~df.age_diff.isna()]
    
    # bucketize age
    agg_diff_vec = df.age_diff.to_numpy()
    categories = np.empty(agg_diff_vec.shape, dtype=object)

    categories[agg_diff_vec < -15] = "much_younger"
    categories[(agg_diff_vec >= -15) & (agg_diff_vec < -7)] = "younger"
    categories[(agg_diff_vec >= -7) & (agg_diff_vec < 7)] = "same_age"
    categories[(agg_diff_vec >= 7) & (agg_diff_vec < 15)] = "older"
    categories[agg_diff_vec >= 15] = "much_older"

    df['age_bucket'] = categories
    
    counts = df.groupby(['target', 'age_bucket']).size().reset_index(name='counts')
    df_wide = counts.pivot(index='target', columns='age_bucket', values='counts').fillna(0).reset_index()
    
    # Preprocess paper data

    df_pap = con.sql("""
        SELECT p.pub_year, p.target
        FROM paper p
        LEFT JOIN author_tidy a
        ON p.aid = a.aid AND p.pub_year = a.pub_year
        WHERE p.pub_year = 2023
    """).fetchdf()

    counts_pap = df_pap.groupby(['target']).size().reset_index(name='nb_papers')

    # Merge paper data to aggregate author data

    df_wide = df_wide.merge(counts_pap, how="left", on=['target'])

    # Load annotation data

    df_annots = pd.read_csv(args.annots / "researchers.tsv", sep="\t", usecols=['oa_display_name', 'has_research_group'])

    # Merge data with annotation data
    df_wide = df_wide.merge(df_annots, how="inner", left_on=['target'], right_on=['oa_display_name'])

    # Output data
    df_wide.to_csv(args.output / "wide_data.csv", index=False)

if __name__ == "__main__":
    main()