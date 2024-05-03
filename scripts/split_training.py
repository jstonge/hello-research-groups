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
    
    df = pd.read_parquet("../data/processed/coauthor_augmented.parquet")

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
    df_pap = pd.read_parquet("../data/processed/paper_tidy.parquet", columns=['pub_year', 'name'])
    counts_pap = df_pap.groupby(['name', 'pub_year']).size().reset_index(name='nb_papers')

    # Merge paper data to aggregate author data
    df_wide = df_wide.merge(counts_pap, how="left", on=['name', 'pub_year'])

    # df_wide[df_wide.nb_papers.isna()]

    # ADD ANNOTATION DATA ABOUT HAVING RESEARCH GROUP
    df_annots = pd.read_csv("../data/raw/researchers.tsv", sep="\t", usecols=['oa_display_name', 'has_research_group'])

    # Merge data with annotation data
    df_wide = df_wide.merge(df_annots, how="inner", left_on=['name'], right_on=['oa_display_name'])

    # Output data
    df_wide.to_csv("../data/training/training_data.csv", index=False)
    df_wide.to_csv("../docs/data/training_data.csv", index=False)
    
    
    
if __name__ == "__main__":
    main()


# d=pd.read_csv("/Users/jstonge1/Downloads/Finding Principal Investigators (PIs) - PIs with a research group(2).tsv", sep="\t") 
# d2=pd.read_csv("/Users/jstonge1/Downloads/Finding Principal Investigators (PIs) - nsf-gov_researchExperienceSites(2).tsv", sep="\t")
# d2=d2[~d2.oa_display_name.isna()]  

# cols = ['oa_display_name',                            
# 'is_prof',                                    
# 'perceived_as_male',                          
# 'host_dept (; delimited if more than one)',   
# 'has_research_group',                         
# 'OpenAlex id',                                
# 'group_url']                           

# d = d[cols]
# d2 = d2[cols]

# d = pd.concat([d,d2], axis=0) 
# d.to_csv("researchers.tsv", sep="\t", index=False) 