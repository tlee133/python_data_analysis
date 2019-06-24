import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# this was a RNA Seq Data Set
# Load data with Pandas
pd.read_csv("").head()

# set the gene_id 
expr_data_w_meta = pd.read_csv("", index_col=0)
expr_data_w_meta.head()

# Checking replicates in the data.
plt.scatter(expr_data_w_meta["baseline_1"],expr_data_w_meta["baseline_2"])
plt.xlabel("Baseline Rep1",fontsize=14)
plt.ylablel("Baseline Rep2",fonstize=14)
plt.show()

from scipy import stats
corr = stats.pearsonr(expr_data_w_meta["baseline_1"],expr_data_w_meta["baseline_3"])
corr

plt.scatter(expr_data_w_meta["baseline_1"],expr_data_w_meta["DE.TMC.day5_1"])
corr = stats.pearsonr(expr_data_w_meta["baseline_1"],expr_data_w_meta["DE.TMC.day5_1"])

# Add a title
plt.title("Pearson Corr:{}".format(np.round(corr[0],3)),fontsize=16)

plt.xlabel("Baseline Rep1",fonsize=14)
plt.ylabel("TMC Day5 Rep1",fontize=14)
plt.show()

