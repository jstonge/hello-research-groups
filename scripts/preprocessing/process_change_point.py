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
    
    # con = duckdb.connect("../../data/clean/oa_data.db")
    con = duckdb.connect(args.input / "oa_data.db")
    
    df = con.sql("""
        SELECT c.pub_date, c.target as ego, a2.aid, c.shared_institutions, a2.author_age as ego_age, a2.first_pub_year as ego_min_year, 
            c.title as coauthor_name, 
            a.pub_year,
            a.first_pub_year as coauthor_min_year,
            c.all_times_collabo, c.yearly_collabo, 
            c.acquaintance,
            a.author_age as coauthor_age,
            (a2.author_age-a.author_age) AS age_diff,
            c.type, c.target_type
        FROM coauthor c
        LEFT JOIN author a
        ON c.aid = a.aid AND c.pub_year = a.pub_year
        LEFT JOIN author a2
        ON c.target = a2.display_name AND c.pub_year = a2.pub_year
        WHERE c.target = ${selected_author}  AND a.pub_year < 2024
        ORDER BY a.pub_year
    """).fetchdf()