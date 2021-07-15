from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from matplotlib import pyplot as plt
import seaborn as sns


def create_cluster_histogram(dataframe, feature):
    print("Generating " + feature + "cluster comparison histogram...")
    # # notify that plot is being generated
    figure = plt.figure()
    sns.histplot(dataframe, x=feature, hue="cluster", element="poly")
    plt.xlabel(feature)
    plt.title("Cluster Comparison of " + feature)
    figure.savefig("plots/clusters/"+feature+".png", dpi=figure.dpi)
    print("Finished. Output saved to "+"plots/clusters/"+feature+".png")  # notify that plot is created


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


def cluster_comparison(k, dataframe, features_list):
    x_data = dataframe[features_list].values
    y_pred = KMeans(n_clusters=k).fit_predict(x_data)
    dataframe["cluster"] = y_pred
    create_cluster_histogram(dataframe, "Total Atk")
    for feature in features_list:
        create_cluster_histogram(dataframe, feature)