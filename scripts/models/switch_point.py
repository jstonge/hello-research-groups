
import os
import pandas as pd
import numpy as np
import arviz as az
import matplotlib.pyplot as plt
import seaborn as sns
from cmdstanpy import CmdStanModel, cmdstan_path
from pathlib import Path

sns.set_style("whitegrid")

ROOT_DIR = Path("../..")
DIR_DAT = ROOT_DIR / "data" / "training"

dat = pd.read_csv(DIR_DAT / 'training_data.csv')

dat_author = dat.query("name == 'Laurent Hébert‐Dufresne'")

stan_file = os.path.join('stan', 'change_point02.stan')
model = CmdStanModel(stan_file=stan_file)

nb_collabs = dat_author.younger.astype(int)
years = dat_author.pub_year.tolist()

sns.scatterplot(x=years, y=nb_collabs)
plt.ylabel("# collab younger")
plt.xlabel("Year")

data  = {
    "T" : len(years),
    "D" : nb_collabs.to_list()
}


fit = model.sample(data=data)
fit_az = az.InferenceData(posterior=fit.draws_xr())
post = fit_az.posterior
trace = post.stack(draws=("chain", "draw"))

az.plot_trace(fit_az, var_names=('e', 'l'))
plt.tight_layout()

# fit.summary()

ys = [np.exp(_[-1]) for _ in trace['lp'].to_numpy()] 
ys /= np.sum(ys)
df=pd.DataFrame({"x":years, "y":ys})
sns.barplot(x='x', y='y', data=df[df.y > 1e-4], color='midnightblue', alpha=0.7);

plt.figure(figsize=(10, 8))
plt.plot(years, nb_collabs, ".", alpha=0.6)
plt.ylabel("Number of accidents", fontsize=16)
plt.xlabel("Year", fontsize=16)

year_s = df.loc[df.y.argmax(), 'x']
plt.vlines(year_s, nb_collabs.min(), nb_collabs.max(), color="C1")
average_disasters = np.zeros_like(nb_collabs, dtype="float")
for i, year in enumerate(years):
    idx = year < year_s
    average_disasters[i] = np.mean(np.where(idx, trace["e"], trace["l"]))


plt.fill_betweenx(
    y=[nb_collabs.min(), nb_collabs.max()],
    x1=df[df.y > 1e-2].min()['x'],
    x2=df[df.y > 1e-2].max()['x'],
    alpha=0.9,
    color="C1",
)
plt.fill_betweenx(
    y=[nb_collabs.min(), nb_collabs.max()],
    x1=df[df.y > 1e-5].min()['x'],
    x2=df[df.y > 1e-5].max()['x'],
    alpha=0.4,
    color="C1",
)
plt.plot(years, average_disasters, "k--", lw=2);


