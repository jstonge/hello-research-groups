import re
import requests
from time import sleep
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm
from pathlib import Path
import argparse

import sys
sys.path.append("..")

from helpers import generate_query

def parse_args():
    parser = argparse.ArgumentParser("Data Downloader")
    parser.add_argument(
        "-o", "--output", type=Path, help="output directory", required=True
    )
    return parser.parse_args()


def main():
    """https://apps.neh.gov/publicquery/default.aspx"""

    # r = requests.get("https://apps.neh.gov/PublicQuery/Default.aspx?q=1&a=0&n=0&o=0&ot=0&k=0&f=0&s=0&cd=0&p=0&d=1&dv=2&at=0&y=0&prd=0&cov=0&prz=0&wp=0&sp=0&ca=0&arp=0&ob=Institution%20name&or=ASC")
    # soup = BeautifulSoup(r.content, "html.parser")
    # table = soup.find("table", class_="rgMasterTable")
    # colnames = table.find_all("th", class_="rgHeader") if table else []
    # colnames = [_.get_text() for _ in colnames]
    # rows = table.find_all("tr", class_="rgRow") if table else []
    # table_dat=[]
    # for row in rows:
    #     cells = row.find_all("td")
    #     cell_data = [cell.get_text(strip=True) for cell in cells]
    #     table_dat.append(cell_data)
    # pd.DataFrame(table_dat, columns=colnames)

    args = parse_args()

    # OUTPUT_DIR = Path("../../data/raw/nsf_humanities")
    OUTPUT_DIR = Path(args.output)

    state_code = ["AL","AK","AZ","AR","CA","CO","CT","DE","DC","FL","GA","HI","ID","IL",
                "IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO",
                "MT","NE","NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR","PA",
                "RI","SC","SD","TN","TX","UT","VT","VA","WA","WV","WI","WY"]

    for code in tqdm(state_code[1:], total=len(state_code[1:])):
        
        # We do not want to assume columns are the same over the years
        # we create a dataframe by year, then we will concat them
        # If columns change, pd.concat will do the right thing.
        dfs = []
        for yr in range(1960, 2023):
            
            table_dat = []
            print(yr)
            url=generate_query(code=code, yr=yr)
            url=f"https://apps.neh.gov/PublicQuery/Default.aspx?q=1&a=0&n=0&o=0&ot=0&k=0&f=0&s=1&sv={code}&cd=0&p=0&d=0&at=1&atv=2&y=1&yf={yr}&yt={yr+1}&prd=0&cov=0&prz=0&wp=0&sp=0&ca=0&arp=0&ob={ob}&or={xor}"
            
            response = requests.get(url)
            soup = BeautifulSoup(response.content, "html.parser")
            
            # find table Master table
            table = soup.find("table", class_="rgMasterTable")

            # grqab columns names
            colnames = table.find_all("th", class_="rgHeader") if table else []
            colnames = [_.get_text() for _ in colnames]

            # Extract data
            rows = table.find_all("tr", class_="rgRow") if table else []
            for row in rows:
                cells = row.find_all("td")
                cell_data = [cell.get_text(strip=True) for cell in cells]
                table_dat.append(cell_data)

            dfs.append(pd.DataFrame(table_dat, columns=colnames))
            

        if len(dfs) > 0:

            # Slow but at least we know concat would do right thing
            df = pd.concat(dfs, axis=0).reset_index(drop=True)

            df.to_parquet(OUTPUT_DIR / f"{code}.parquet")

