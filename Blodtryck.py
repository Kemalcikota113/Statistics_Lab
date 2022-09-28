from cmath import sqrt
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as plt
from scipy.stats import norm

# read data files using Pandas
headers = ['x', 'y']
df = pd.read_csv('blodtryck.csv', header=None, names=headers)

# plt.style.use("dark_background")

print(df.head())
sns.scatterplot(data=df, x='x', y='y')
# sns.lineplot(data=df, x='x', y='y')   # lineplot will not give us a usefull graph for this sort of data.
plt.pyplot.show()

f = sns.regplot(data=df, x='x', y='y')
plt.pyplot.show()

x = df['x'].tolist()
y = df['y'].tolist()
medelx = df['x'].mean()
medely = df['y'].mean()

vxx = 0
vxy = 0

for item in x:
    vxx += (item - medelx)**2

n = 0

while n < len(df):
    vxy += (x[n] - medelx) * (y[n] - medely)
    n += 1

idk = 0

for item in x:
    idk += item**2

k_hat = vxy/vxx

print("k hat:", k_hat)

# m_hat = norm.pdf(70, ((vxx*idk)/(len(df)*vxy)))
print("m hat:", medely - (k_hat*medelx))

# inte orimligt. <==> rimligt

Yk = 0
sigmaYk2 = 0

# for item in y:
#     Yk += item

# for item in y:
#     sigmaYk2 += item**2

# Syy = sigmaYk2 - ((Yk^2)/len(df))

Syy = 0
for item in y:
    Syy += (item - medely)**2

t0025 = 2.1

s2 = (Syy - ((vxy**2)/vxx))/(len(df)-2)

s = sqrt(s2)

iplus = k_hat + (t0025* (s/sqrt(vxx)))
iminus = k_hat - (t0025* (s/sqrt(vxx)))

print("Intervall: [%s, %s]" % (iminus, iplus))
print(vxx, vxy, Syy)
# 4  ----------------------------------------------
standard_x = np.std(x)
standard_y = np.std(y)

Cxy = 0
n = 0

while n < len(x):
    Cxy += ((x[n])*(y[n]))
    n+=1
Cxy -= ((len(x)*medelx*medely))
Cxy = Cxy/(len(x)-1)

print("r:", (Cxy/(standard_x*standard_y)))      # hög positiv korrelation, betyder att värdena ökar med hog korrelation.

# 5
Zscores = []

for item in y:
    a = (item-medely)/standard_y
    Zscores.append(a)

Zscores.sort()

print(Zscores[0])
print(Zscores[len(Zscores)-1])
zlow = medely - (max(Zscores)*standard_y/sqrt(len(y)))
zhigh = medely + (max(Zscores)*standard_y/sqrt(len(y)))
print("confidence interval: [%s, %s]" % (zlow, zhigh))