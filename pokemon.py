import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

# Research Questions #

# Unsupervised: If I graph every pokemon, do the nets stats change as generation changes?
# Supervised: If a new pokemon is found in the wild, can I classify whether it is a legendary pokemon or not?

# Part 1: Data Input #

# Convert CSV to DataFrame for Pandas
df = pd.read_csv("data/Pokemon.csv", engine="python")

# print(df.head(4))


# Part 2: Data Visualization #

WEAK_THRESHOLD = 200
MOD_THRESHOLD = 400


def power(row):
    if row["Total"] < WEAK_THRESHOLD:
        return "weak"
    elif row["Total"] < MOD_THRESHOLD:
        return "moderate"
    else:
        return "strong"


df["Power"] = df.apply(power, axis=1)
print(df[["Name", "Power"]].head(5))

plt.scatter(df["#"], df["Total"], linewidth=2.0)
plt.xlabel("#")
plt.ylabel("Total")
plt.title("Total versus #")
plt.show()

fig, ax = plt.subplots()
colors = {'weak': 'red', 'moderate': 'green', 'strong': 'blue'}
grouped = df.groupby('Power')

for key, group in grouped:
    group.plot(ax=ax, kind='scatter', x='Generation', y='Total', label=key, color=colors[key])

ax.set_title('Total vs Generation')
plt.show()

plt.hist([df["Power"]], bins=7, )
plt.show()

# Pokemon Name Versus Attack Stat

# plt.plot(df.Name[0:3], df.Attack[0:3], linewidth=2.0)
# plt.xlabel("Pokemon Name")
# plt.ylabel("Attack Stat")
# plt.title("Pokemon Name versus Attack Stat")
# plt.show()
