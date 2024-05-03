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
        "-o", "--output", type=Path, help="output directory", required=True
    )
    return parser.parse_args()

def main():
    
    args = parse_args()
    
    con = duckdb.connect("../../data/raw/oa_data_raw.db")

    query = """
        SELECT p.ego_aid, a.display_name as name, p.pub_date, p.pub_year, p.title,
               p.cited_by_count, p.doi, p.wid, 
               a.author_age as ego_age, a.pub_year as pub_year2
        FROM paper p
        LEFT JOIN author_tidy a ON p.ego_aid = a.aid AND p.pub_year = a.pub_year
    """


    df = con.sql(query).fetchdf()

    # DROP PAPERS W/O TITLE
    df = df[~df.title.isna()]

    # deduplicate papers by title and aid.
    # We grab the most recent papers.
    df = df.sort_values("pub_date", ascending=False).reset_index(drop=True)
    # df = df.query("ego_aid == 'A5065482485'")
    df['title'] = df.title.str.lower()
    df = df[~df[['ego_aid', 'title']].duplicated()]

    # DROP PAPERS WITH "TABLE" IN TITLE
    df = df[~df.title.str.contains("Table", case=False)]
    df = df[~df.title.str.contains("Appendix", case=False)]
    df = df[~df.title.str.contains("Issue Information", case=False)]
    df = df[~df.title.str.contains("Issue Cover", case=False)]
    df = df[~df.title.str.contains("Peer Review", case=False)]
    df = df[~df.title.str.contains("This Week in Science", case=False)]
    df = df[~df.title.str.contains("^Figure ", case=False)]
    df = df[~df.title.str.contains("^Data for ", case=False)]
    df = df[~df.title.str.contains("^Author Correction: ", case=False)]
    df = df[~df.title.str.contains("supporting information", case=False)]

    df.to_parquet("../../data/processed/paper_tidy.parquet")
    df.to_parquet("../../docs/data/paper_tidy.parquet")

    con.close()
    
if __name__ == "__main__":
    main()