import pandas as pd
import numpy as np
import argparse
from pathlib import Path
from itertools import combinations
from collections import Counter
import json

def flatten(l):
    return [item for sublist in l for item in sublist]
    
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
    
    # INPUT_DIR = Path("../data/processed/")
    # ANNOT_DIR = Path("../data/raw/")
    # OUTPUT_DIR = Path("../data/training/")
    INPUT_DIR = args.input 
    ANNOT_DIR = args.annots
    OUTPUT_DIR = args.output
    
    df = pd.read_csv(INPUT_DIR / "coauthor.csv")

    # FOR NOW WE REMOVE THOSE WITH MISSING AGE BUCKET
    df = df[~df.age_bucket.isna()].reset_index(drop=True)

    # More coarse-grained age buckets
    df['age_bucket'] = np.where(df.age_bucket == 'much_younger', 'younger', df.age_bucket)
    df['age_bucket'] = np.where(df.age_bucket == 'much_older', 'older', df.age_bucket)

    counts = df.groupby(['name', 'age_bucket', 'pub_year']).size().reset_index(name='counts')
    df_wide = counts.pivot(index=['name', 'pub_year'], columns='age_bucket', values='counts').fillna(0).reset_index().sort_values(['name', 'pub_year'])

    # standardized age 
    df_wide = df_wide.merge(df[~df[['name', 'pub_year']].duplicated()][['name', 'pub_year', 'author_age']], on=['name', 'pub_year'], how='left')
    
    # new acquaintance
    counts_new_acq = df.groupby(['name', 'acquaintance', 'pub_year']).size().reset_index(name='counts')
    df_wide_new_acq = counts_new_acq.pivot(index=['name', 'pub_year'], columns='acquaintance', values='counts').fillna(0).reset_index().sort_values(['name', 'pub_year'])
    df_wide = df_wide.merge(df_wide_new_acq, on=['name', 'pub_year'], how='left')

    df_shared_inst = df[~df.shared_institutions.isna()]
    counts_shared_inst = df_shared_inst.groupby(['name', 'age_bucket', 'pub_year', 'shared_institutions']).size().reset_index(name='counts')
    df_wide_shared_inst = counts_shared_inst.pivot(index=['name', 'pub_year'], columns='age_bucket', values='counts').fillna(0).reset_index().sort_values(['name', 'pub_year'])
    df_wide = df_wide.merge(df_wide_shared_inst, on=['name', 'pub_year'], how='left', suffixes=('', '_shared_inst'))

    
    df_wide['prop_younger'] = df_wide.younger / (df_wide.older+df_wide.younger+df_wide.same_age)
    df_wide['total_coauth'] = df_wide.older + df_wide.younger + df_wide.same_age


    # ADD PAPER DATA
    df_pap = pd.read_csv(INPUT_DIR / "paper.csv")
    counts_pap = df_pap[['name', 'pub_year']].groupby(['name', 'pub_year']).size().reset_index(name='nb_papers')

    # Merge paper data to aggregate author data
    df_wide = df_wide.merge(counts_pap, how="left", on=['name', 'pub_year'])

    # Calculate density of matrix of coauthors by year
    out = {}
    for auth in df_pap.name.unique():
        df_coauths_mat = df_pap.loc[df_pap.name == auth, ['wid', 'name', 'authors', 'pub_year']]\
                            .assign(authors = lambda x: x.authors.map(lambda x: x.split(", ")))\
                            .explode('authors')\
                            .sort_values('pub_year')\
                            .query(f'authors != "{auth}"')\
                            .rename(columns={'authors': 'coauth_name'})
        
        df_coauths_mat = df_coauths_mat.merge(df[['name', 'pub_year', 'coauth_name', 'age_bucket']], on=['name', 'pub_year', 'coauth_name'])
        
        def extract_comb_coauths(x):
            return list(combinations(df_coauths_mat.loc[df_coauths_mat.wid == x, ['wid', 'pub_year', 'coauth_name']].coauth_name, 2))

        
        for year in df_coauths_mat.pub_year.unique():
            tmp_df = df_coauths_mat[(df_coauths_mat.age_bucket == 'younger') & (df_coauths_mat.pub_year == year)]
            comb_auths = [extract_comb_coauths(wid) for wid in tmp_df.wid.unique()]
            count_auths = Counter(flatten(comb_auths))
            
            if len(count_auths) > 0:
                df_long = pd.DataFrame(count_auths.keys(), columns=['source', 'target']).assign(nb_collab = count_auths.values())
                df_long[['source', 'target']] = pd.DataFrame(np.sort(df_long[['source', 'target']], axis=1))    
                aggregated_df = df_long.groupby(['source', 'target'], as_index=False)['nb_collab'].sum()
                matrix = aggregated_df.pivot_table(index='source', columns='target', values='nb_collab', fill_value=0)
                
                # calculate density
                non_zero_edges = np.count_nonzero(np.triu(matrix, k=1))
                num_nodes = matrix.shape[0]
                total_possible_edges = (num_nodes * (num_nodes - 1)) / 2
                density = np.round((non_zero_edges / total_possible_edges), 3) if total_possible_edges > 0 else 0
                out[(auth, year)] = density
            else:
                out[(auth, year)] = 0

    df_wide['density'] = df_wide.apply(lambda row: out.get((row['name'], row['pub_year']), None), axis=1)

    # ADD ANNOTATION DATA ABOUT HAVING RESEARCH GROUP
    df_annots = pd.read_csv(ANNOT_DIR / "researchers.tsv", sep="\t")


    df_annots.rename(columns={'host_dept (; delimited if more than one)': 'department'}, inplace=True)
    df_annots['department'] = df_annots.department.str.split("; ")
    df_annots = df_annots.explode("department")
    
    # see uToronto Arts and Sci: https://www.artsci.utoronto.ca/future/academic-opportunities/explore-our-programs
    # see UVM colleges https://catalogue.uvm.edu/undergraduate/aboutuniv/
    # see McGill faculties https://www.mcgill.ca/faculties/ (agricultural & environmental, arts, dental, education, engineering, law, management, medicine+health sciences, music, science)
    # see harvard https://www.harvard.edu/academics/schools/ (education, design, dental+medicine, business, FAS, engineering and applied sciences, law, public health)
    # see stanford https://www.stanford.edu/list/academic/ (business, education, engineering, humanities & sciences, law, medicine, sustainability)
    dept2fos = json.loads(open(ANNOT_DIR / "dept2fos.json").read() )
    dept2fos = {v['department']:v['category'] for v in dept2fos}
 
    df_annots['college'] = df_annots.department.map(lambda x: dept2fos[x] if dept2fos.get(x) else None)
    df_annots.loc[df_annots['college'].isna(),['department', 'college']]
 

    # Merge data with annotation data
    df_wide = df_wide.merge(df_annots, how="inner", left_on=['name'], right_on=['oa_display_name'])

    # Output data
    df_wide.to_csv(OUTPUT_DIR / "training_data.csv", index=False)
    
    
    
if __name__ == "__main__":
    main()



# d=pd.read_csv("/Users/jstonge1/Downloads/Finding Principal Investigators (PIs) - PIs with a research group(7).tsv", sep="\t") 
# df = pd.read_csv(INPUT_DIR / "author.csv")
# d = d.merge(df.loc[df.pub_year == 2023, ['display_name', 'institution']].drop_duplicates(), left_on='oa_display_name', right_on='display_name', how='left')
# d.to_csv("~/test.csv", index=False)

# d=pd.read_csv("/Users/jstonge1/Downloads/Finding Principal Investigators (PIs) - PIs with a research group(7).tsv", sep="\t") 
# d2=pd.read_csv("/Users/jstonge1/Downloads/Finding Principal Investigators (PIs) - nsf-gov_researchExperienceSites(4).tsv", sep="\t")
# d2=d2[~d2.oa_display_name.isna()]  

# cols = ['oa_display_name', 'is_prof', 'group_size', 'perceived_as_male', 
#         'host_dept (; delimited if more than one)',   'has_research_group', 'OpenAlex id', 'group_url'] 

# d = d[cols]
# d2 = d2[cols]

# d = pd.concat([d,d2], axis=0) 
# d.to_csv(ANNOT_DIR / "researchers.tsv", sep="\t", index=False) 

