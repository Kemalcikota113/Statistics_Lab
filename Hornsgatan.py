from random import random
import numpy as np
import pandas as pd
from scipy.stats import norm
import seaborn as sns
import matplotlib as plt

# read data files using Pandas
df = pd.read_csv("PM25.csv")

df_2008 = df.loc[df["Year"]==2008]
df_2010 = df.loc[df["Year"]==2010]

mu = df_2010["PM25"].mean()
sigma = df_2010["PM25"].std()
n = len(df_2010)

new_random = np.random.normal(mu, sigma, 10000000)      #10000000
x = np.linspace(-5, 25, 10000000)
y = norm.pdf(x, mu, sigma)

sns.histplot(data=new_random, stat='density',)
#sns.lineplot(x, y, color="red")

plt.pyplot.show()

# cdf = norm.cdf(x, new_random)
# sns.histplot(data=cdf)
# plt.pyplot.show()
# print("cdf:", cdf)
