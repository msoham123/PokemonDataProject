import pandas as pd
import numpy as np
import seaborn as sns
import scripts.scatterplot_matrix
import scripts.power_histogram
import scripts.stats_scatterplot

# Part 1: Data Input #

# Convert CSV to DataFrame for Pandas
df = pd.read_csv("data/Pokemon.csv", engine="python")

# Part 2: Data Visualization #
# Uncomment the following lines to regenerate plots

# scripts.scatterplot_matrix.create_scatterplot_matrix(df, "Legendary")
# scripts.power_histogram.create_power_histogram(df)
# scripts.stats_scatterplot.create_scatterplot(df, "Attack", "Sp. Atk")
# scripts.stats_scatterplot.create_scatterplot(df, "Defense", "Sp. Def")

# Part 3: Feature Engineering #

# By looking at plots/Sp. AtkversusAttack.png and
# plots/Sp. DefversusDefense.png, we can see that for the most
# part, a stat and it's special counterpart are correlated.

# Therefore, we can abstract these categories by creating two
# new stat groups, Total Atk and Total Def

df["Total Atk"] = df["Attack"] + df["Sp. Atk"]
df["Total Def"] = df["Defense"] + df["Sp. Def"]

# Part 4: Clustering #
































#
# plt.scatter(df["#"], df["Total"], linewidth=2.0)
# plt.xlabel("#")
# plt.ylabel("Total")
# plt.title("Total versus #")
# plt.show()
#
# fig, ax = plt.subplots()
# colors = {'weak': 'red', 'moderate': 'green', 'strong': 'blue'}
# grouped = df.groupby('Power')
#
# for key, group in grouped:
#     group.plot(ax=ax, kind='scatter', x='Generation', y='Total', label=key, color=colors[key])
#
# ax.set_title('Total vs Generation')
# plt.show()
#





# Pokemon Name Versus Attack Stat

# plt.plot(df.Name[0:3], df.Attack[0:3], linewidth=2.0)
# plt.xlabel("Pokemon Name")
# plt.ylabel("Attack Stat")
# plt.title("Pokemon Name versus Attack Stat")
# plt.show()
