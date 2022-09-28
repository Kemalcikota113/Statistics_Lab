import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as plt

df_USA = pd.read_csv("JordgubbUSA.csv")
df_UNGERN = pd.read_csv("JordgubbUngern.csv")

sns.lineplot(data=df_USA, x="Year", y="Prod", marker='o')
plt.pyplot.show()

sns.lineplot(data=df_UNGERN, x="Year", y="Prod", marker='o')
plt.pyplot.show()

# Linje diagram, eftersom vi kan lätt se förändring av data över åren, förändringen av mängden jordgubbar producerade under årens gång.
# mängden Jordgubbar producerade i Ungern är mycket mindre än mängden producerade i USA. 
# Sammt har mängden som produceras i USA ökat medans mängden i Ungern minskat.

standard_USA = df_USA["Prod"].std()
standard_UNGERN = df_UNGERN["Prod"].std()
medel_USA = df_USA["Prod"].mean()
medel_UNGERN = df_UNGERN["Prod"].mean()

Cxy = 0
n = 0

while n < 22:
    Cxy += ((df_USA["Prod"][n])*(df_UNGERN["Prod"][n]))
    n+=1
Cxy -= ((22*medel_USA*medel_UNGERN))
Cxy = Cxy/(21)

print("r:", (Cxy/(standard_USA*standard_UNGERN)))

# liten till ingen korrelation. korellation implicerar ej kausalitet.