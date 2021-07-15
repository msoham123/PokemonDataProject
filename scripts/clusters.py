from sklearn.cluster import KMeans
import pandas


def cluster_stats(k, dataframe, stat_one, stat_two, stat_three):
    print(len(dataframe[stat_one]))
    classifier = KMeans(n_clusters=k).fit_predict(
        dataframe[[stat_one, stat_two, stat_three]].values
    )

