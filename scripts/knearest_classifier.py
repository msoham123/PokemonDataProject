from sklearn.neighbors import KNeighborsClassifier
from matplotlib import pyplot as plt


def create_nearest_classifier_plot(k, dataframe, x_features, y_feature, split):
    print("Generating neighbors plot...")
    scores = []
    df = dataframe[:split]
    length = range(2, k)
    for n in length:
        classifier = KNeighborsClassifier(n_neighbors=n)
        x_train = df[x_features].values
        y_train = df[y_feature]
        classifier.fit(x_train, y_train)
        scores.append(test_nearest_classifier(classifier, dataframe, x_features, y_feature, split))
    figure = plt.figure()
    plt.plot(length, scores)
    plt.xlabel("Number of Neighbors")
    plt.ylabel("KNN Score")
    figure.savefig("plots/neighbors_plot.png", dpi=figure.dpi)
    print("Finished. Output saved to plots/neighbors_plot.png.")
    classifier = KNeighborsClassifier(n_neighbors=scores.index(max(scores))+1)
    x_train = df[x_features].values
    y_train = df[y_feature]
    classifier.fit(x_train, y_train)
    return classifier


def test_nearest_classifier(classifier, dataframe, x_features, y_feature, split):
    df_test = dataframe[split:]
    x_test = df_test[x_features].values
    y_test = df_test[y_feature]
    score = classifier.score(x_test, y_test)
    return score
