import pandas as pd
from pathlib import Path


def main():
    input_dir = Path("../../data/raw/nsf_humanities")
    output_dir = Path("../../data/clean/")
    fnames = list(input_dir.glob("*.parquet"))
    dfs = []
    for fname in fnames:
        # thissss is sloow but whatev forn now
        dfs.append(pd.read_parquet(fname))
    
    all_df = pd.concat(dfs, axis=0).reset_index(drop=True)
    
    # columns
    all_df.columns = all_df.columns.str.lower()
    all_df.columns = all_df.columns.str.replace(" ", "_")
    
    # start-end as their own column
    all_df[['start_date', 'end_date']] = all_df.award_period.str.split("-", expand=True)
    all_df['start_date'] = pd.to_datetime(all_df['start_date'])
    
    # useful columns
    all_df['pub_year'] = all_df['start_date'].dt.year

    all_df['approved_award_total'] = all_df.approved_award_total.str.replace("(\$|,|\.)", "", regex=True).astype(int)

    all_df.value_counts('pub_year', ascending=True).sort_index().plot()
    
    all_df['nsf_name'] = all_df.project_director_first_name + " " + all_df.project_director_middle_name + " " + all_df.project_director_last_name 


    all_df.to_parquet(output_dir / "nsf_humanities.parquet")
        

if __name__ == "__main__":
    main()