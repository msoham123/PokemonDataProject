from matplotlib import pyplot as plt


def create_scatterplot(dataframe, stat_one, stat_two):
    print("Generating scatterplot between", stat_one, "and", stat_two, "...")
    figure = plt.figure()
    plt.scatter(dataframe[stat_one], dataframe[stat_two], linewidth=2.0)
    plt.xlabel(stat_one)
    plt.ylabel(stat_two)
    plt.title(stat_two + " versus " + stat_one)
    figure.savefig("plots/"+stat_two+"versus"+stat_one+".png", dpi=figure.dpi)
    print("Finished. Output saved to " + "plots/"+stat_two+"versus"+stat_one+".png")
