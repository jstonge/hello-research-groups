import duckdb
import pandas as pd
import numpy as np
import argparse
import numpy as np
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
    
    # con = duckdb.connect("../../data/raw/oa_data_raw.db")
    con = duckdb.connect(str(args.input / "oa_data_raw.db"))

    query = """
        SELECT * FROM author_tidy
    """

    df = con.sql(query).fetchdf()

    def gen_fill_char(lower, upper):
        return np.char.zfill(np.random.randint(lower,upper,len(df)).astype(str),2)
    
    df["age_std"] = "1"+df.author_age.astype(str).map(lambda x: x.zfill(3))+"-"+gen_fill_char(1, 12)+"-"+gen_fill_char(1, 28)
    
    df.to_csv(args.output / "author.csv", index=False)
    
    con.close()

if __name__ == "__main__":
    main()