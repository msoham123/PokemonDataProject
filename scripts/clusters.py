from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from matplotlib import pyplot as plt


def cluster_stats(k, dataframe, features_list):
    print("Generating cluster plot...")
    silhouettes = []
    length = range(2, k)
    x_data = dataframe[features_list].values
    for n_clusters in length:
        y_pred = KMeans(n_clusters=n_clusters).fit_predict(x_data)
        silhouettes.append(silhouette_score(x_data, y_pred))
    figure = plt.figure()
    plt.plot(length, silhouettes)
    plt.xlabel("Number of Clusters")
    plt.ylabel("Silhouette Score")
    figure.savefig("plots/clusters_plot.png", dpi=figure.dpi)
    print("Finished. Output saved to plots/clusters_plot.png.")
