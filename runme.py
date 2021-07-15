import pandas as pd
import scripts.scatterplot_matrix
import scripts.power_histogram
import scripts.stats_scatterplot
import scripts.regression_plot
import scripts.clusters

# Part 1: Data Input #

# Convert CSV to DataFrame for Pandas
df = pd.read_csv("data/Pokemon.csv", engine="python")

# Part 2: Data Visualization #

# Comment the following lines to not regenerate plots
# scripts.scatterplot_matrix.create_scatterplot_matrix(df, "Legendary")
# scripts.power_histogram.create_power_histogram(df)
# scripts.stats_scatterplot.create_scatterplot(df, "Attack", "Sp. Atk")
# scripts.stats_scatterplot.create_scatterplot(df, "Defense", "Sp. Def")


# Part 3: Feature Engineering #

# By looking at plots/Sp. AtkversusAttack.png and plots/Sp. DefversusDefense.png, we can see that for the most part,
# a stat and it's special counterpart are correlated. Therefore, we can abstract these categories by creating two new
# stat groups, Total Atk and Total Def

df["Total Atk"] = df["Attack"] + df["Sp. Atk"]
df["Total Def"] = df["Defense"] + df["Sp. Def"]

types = ["Normal", "Fire", "Water", "Grass", "Electric",
         "Ice", "Fighting", "Poison", "Ground", "Flying",
         "Psychic", "Bug", "Rock", "Ghost", "Dark",
         "Dragon", "Steel", "Fairy"]

for index, row in df.iterrows():
    for pokemon_type in types:
        if row[2] == pokemon_type:
            df.loc[index, pokemon_type] = 1
        elif row[3] == pokemon_type:
            df.loc[index, pokemon_type] = 1
        else:
            df.loc[index, pokemon_type] = 0

# As a thought experiment, why don't we compare Total Atk and Total Def together?
# Comment the following line to not regenerate plot
# scripts.regression_plot.create_regression_plot(df, "Total Atk", "Total Def")


# Part 4: Clustering #

feature_list = ["Total Atk", "Total Def", "Speed", "HP"] + types

print(feature_list)

scripts.clusters.cluster_stats(20, df, feature_list)
