from sklearn.cluster import KMeans
import pandas


def cluster_stats(k, dataframe, stat_one, stat_two, stat_three):
    classifier = KMeans(n_clusters=k).fit_predict([dataframe[stat_one], dataframe[stat_two], dataframe[stat_three]])
