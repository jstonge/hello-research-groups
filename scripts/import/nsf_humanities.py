import re
import requests
from time import sleep
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm
from pathlib import Path
import argparse
from time import sleep

from numpy.random import uniform
from selenium.webdriver.common.by import By
from selenium import webdriver



import sys
sys.path.append("..")

# from ..helpers import generate_query

def parse_args():
    parser = argparse.ArgumentParser("Data Downloader")
    parser.add_argument(
        "-o", "--output", type=Path, help="output directory", required=True
    )
    return parser.parse_args()


def main():
    """https://apps.neh.gov/publicquery/default.aspx"""
    
    driver = webdriver.Firefox()
    
    for yr in range(1978, 1981):
        dfs = []
        base_url = 'https://apps.neh.gov/PublicQuery/Default.aspx?'
        all_rows = []
        for atv in [1,2]: # orgs, people
            
            query = f"q=1&a=0&n=0&o=0&ot=0&k=0&f=0&s=0&cd=0&p=0&d=0&at=1&atv={atv}&y=1&yf={yr}&yt={yr+1}&prd=0&cov=0&prz=0&wp=0&sp=0&ca=0&arp=0&ob=Institution%20name&or=ASC"
                        
            url = base_url + query
            driver.get(url)
            sleep(uniform(4))

            soup = BeautifulSoup(driver.page_source, "html.parser")
            table = soup.find("table", class_="rgMasterTable")
            
            try:
                tot_rows, tot_pages = [int(_.get_text()) for _ in table.find("div", class_="rgWrap rgInfoPart") if _.get_text().isnumeric()]
            except:
                continue
            
            
            for i in tqdm(range(tot_pages), total=tot_pages):
            # for i in tqdm(range(5, tot_pages)):
                soup = BeautifulSoup(driver.page_source, "html.parser")
                table = soup.find("table", class_="rgMasterTable")
                
                colnames = table.find_all("th", class_="rgHeader") if table else []
                colnames = [_.get_text() for _ in colnames]
                rows = table.find_all("tr", class_=["rgRow", "rgAltRow"]) if table else []
                table_dat=[]
                for row in rows:
                    cells = row.find_all("td")
                    cell_data = [cell.get_text(strip=True) for cell in cells]
                    table_dat.append(cell_data)
                
                
                df = pd.DataFrame(table_dat, columns=colnames)
                df['Recipient Type'] = 'institutions' if atv == 1 else 'individuals'
                dfs.append(df)
                driver.find_element(By.CSS_SELECTOR, "button.t-button.rgActionButton.rgPageNext").click()
                sleep(uniform(6,7))

            all_rows.append(tot_rows)

        all_dfs = pd.concat(dfs)

        all_dfs = all_dfs[~all_dfs['Award Number\xa0'].duplicated()]
        
        current_an_inst = all_dfs[all_dfs['Recipient Type'] == 'institutions']['Award Number\xa0'].unique()
        assert len(current_an_inst) == all_rows[0]
        
        current_an_inds = all_dfs[all_dfs['Recipient Type'] == 'individuals']['Award Number\xa0'].unique()
        assert len(current_an_inds) == all_rows[1]

        # all_dfs[all_dfs['Award Number\xa0'] == 'FT-23244-83']

        all_dfs.to_parquet(f"../../data/raw/nsf_humanities/{yr}.parquet")

    driver.quit()