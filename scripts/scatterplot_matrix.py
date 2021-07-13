import seaborn as sns
from matplotlib import pyplot as plt


def create_scatterplot_matrix(dataset, hue):
    print("Generating scatterplot matrix....")
    figure = sns.pairplot(dataset, hue=hue)
    figure.fig.set_size_inches(9, 6.5)
    plt.show()
    print("Finished")
