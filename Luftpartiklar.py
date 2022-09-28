import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as plt

# read data files using Pandas
df = pd.read_csv("PM25.csv")

df_2008 = df.loc[df["Year"]==2008]
df_2010 = df.loc[df["Year"]==2010]

print(df_2008)
print(df_2010)

K = sns.histplot(data=df_2008["PM25"])
plt.pyplot.show()

K = sns.histplot(data=df_2010["PM25"])
plt.pyplot.show()

max_08 = df_2008["PM25"].max()
min_08 = df_2008["PM25"].min()
medel_08 = df_2008["PM25"].mean()
standard_08 = df_2008["PM25"].std()
median_08 = df_2008["PM25"].median()
print("max 2008:", max_08)
print("min 2008:", min_08)
print("medel 2008:", medel_08)
print("standardavvikelse 2008:", standard_08)
print("median 2008:", median_08)
print()

max_10 = df_2010["PM25"].max()
min_10 = df_2010["PM25"].min()
medel_10 = df_2010["PM25"].mean()
standard_10 = df_2010["PM25"].std()
median_10 = df_2010["PM25"].median()
print("max 2010:", max_10)
print("min 2010:", min_10)
print("medel 2010:", medel_10)
print("standardavvikelse 2010:", standard_10)
print("median 2010:", median_10)
print()

x = df_2010
y = df_2008
z = np.concatenate([x,y])

plotdf = pd.DataFrame(data=z, columns=["Year", "PM25"])        # data=z

sns.boxplot(data=plotdf, x='PM25', y='Year', orient='h')
plt.pyplot.show()

 # 1.1. Mätdatan tycks vara underlig. Varför finns det mer partiklar efter förbudet än innan. Varför finns det partiklar alls om det är förbud.
 # Vid jämnförelse av medel och median så har dessa värden sjunkit från 2008 till 2010.
 # chansen för att få ett PM som överstiger 25 för 2008 är 4/132 = 0.03, chansen för 2010 är 2/133 = 0.015



 # antalet gånger värdet översteg 25 / antalet mätresultat = relativ frekvens

rf_2008 = len(list(filter(lambda x: x >= 25, df_2008["PM25"])))
rf_2010 = len(list(filter(lambda x: x >= 25, df_2010["PM25"])))

rf_2008_2 = len(list(filter(lambda x: x >= 8.5, df_2008["PM25"])))
rf_2010_2 = len(list(filter(lambda x: x >= 8.5, df_2010["PM25"])))

print("relativ frekvens >= 25, 2008:", rf_2008/len(df_2008))
print("relativ frekvens >= 25, 2010:", rf_2010/len(df_2010))

print("relativ frekvens >= 8.5, 2008:", rf_2008_2/len(df_2008))
print("relativ frekvens >= 8.5, 2010:", rf_2010_2/len(df_2010))

