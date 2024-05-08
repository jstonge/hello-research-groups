import pandas as pd
from pathlib import Path


def main():
    input_dir = Path("../../data/raw/nsf_humanities")
    output_dir = Path("../../docs/data")
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
    

    all_df['approved_award_total'] = all_df.approved_award_total.str.replace("(\$|,|\.)", "", regex=True).astype(int)

    all_df['year_awarded'] = all_df.year_awarded.astype(int)

    # all_df.value_counts('pub_year', ascending=True).sort_index().plot()
    
    cols2keep = ['grant_program_name', 'award_recipient', 'project_title', 'year_awarded', 'approved_award_total', 'division_or_office', 'primary_humanities_discipline']

    all_df = all_df[cols2keep]
    all_df = all_df[(all_df.year_awarded > 1960) & (all_df.year_awarded < 2024)]
    all_df.to_parquet(output_dir / "nsf_humanities.parquet")
        

if __name__ == "__main__":
    main()