from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


def create_regression_plot(dataframe, stat_one, stat_two):
    print("Generating linear regression plot between " + stat_one + " and " + stat_two + "...")
    lin_regress = LinearRegression()
    x = dataframe[stat_one].values.reshape(-1, 1)  # note this is necessary if only one feature
    y = dataframe[stat_two]
    lin_regress.fit(x, y)  # Create a regression model
    lin_predict = lin_regress.predict(x)  # Predict values based on regression model
    figure = plt.figure()
    plt.scatter(x, y, color='black')  # plot the actual data as black circles
    plt.xlabel(stat_one)
    plt.ylabel(stat_two)
    plt.title(stat_one + " versus " + stat_two)
    plt.plot(x, lin_predict, 'cs')  # plot the expected results from the regression as cyan
    figure.savefig("plots/"+stat_one+"versus"+stat_two+"_lreg.png", dpi=figure.dpi)
    print("Finished. Output saved to " + "plots/"+stat_one+"versus"+stat_two+"_lreg.png")

