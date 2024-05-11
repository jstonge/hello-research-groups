
import os
import pandas as pd
import numpy as np
import arviz as az
import seaborn as sns
from cmdstanpy import CmdStanModel
from pathlib import Path
import argparse
import matplotlib.pyplot as plt
from  matplotlib.ticker import FuncFormatter
import numpy as np
from changeforest import changeforest


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




INPUT_DIR = Path("../../data/training")
OUTPUT_DIR = Path("../../data/training")
# args = parse_args()
# INPUT_DIR = args.input
# OUTPUT_DIR = args.output
ROOT_DIR = Path(__file__).resolve().parents[2]

dat = pd.read_csv(INPUT_DIR / 'training_data.csv')
dat_auth = dat[dat.name == 'Adam K. Anderson']
X = dat_auth.younger.to_numpy().reshape(-1, 1)

result = changeforest(X, "random_forest", "bs")
sns.scatterplot(x=range(len(X)), y='younger', data=dat_auth)
plt.vlines(result.split_points(), ymin=0, ymax=X.max(), color='red')
