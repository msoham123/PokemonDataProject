import seaborn as sns


def create_scatterplot_matrix(dataframe, hue):
    print("Generating scatterplot matrix...")
    figure = sns.pairplot(dataframe, hue=hue)
    figure.fig.set_size_inches(9, 6.5)
    figure.savefig("plots/scatterplot_matrix.png", dpi=figure.fig.dpi)
    print("Finished. Output saved to plots/scatterplot_matrix.png.")
