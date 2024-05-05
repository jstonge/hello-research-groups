import re
import requests
from time import sleep
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm
from pathlib import Path
import argparse

# OUTPUT_DIR = Path("../../data/raw/nsf_awards")


def parse_args():
    parser = argparse.ArgumentParser("Data Downloader")
    parser.add_argument(
        "-o", "--output", type=Path, help="output directory", required=True
    )
    return parser.parse_args()

# NSF AWARDS


def nsf_awards():
    """https://www.nsf.gov/awardsearch/download.jsp"""
    
    args = parse_args()
    OUTPUT_DIR = Path(args.output)

    download_awards_by_year_url="https://www.nsf.gov/awardsearch/download.jsp"
    response = requests.get(download_awards_by_year_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        
        download_links = soup.select('.download a[href]')

        # Extract the href attributes
        hrefs = [link['href'] for link in download_links if link['href'].startswith("download")]

    for href in hrefs:
        url=f"https://www.nsf.gov/awardsearch/{href}"
        response = requests.get(url)
        
        if response.status_code == 200:
            if bool(re.search(r"\d{4}", href)):
                year=re.findall(r"\d{4}", href)[0]
                with open(OUTPUT_DIR / f"{year}.zip", "wb") as file:
                    file.write(response.content)
            print(f"Download complete and saved to {year}.zip")
        else:
            print("Failed to retrieve data: Status code", response.status_code)
        
        sleep(0.1)

if __name__ == "__main__":
    nsf_awards()