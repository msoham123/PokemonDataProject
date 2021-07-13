from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


def create_regression_plot(dataframe, stat_one, stat_two):
    print("Generating linear regression plot between " + stat_one + " and " + stat_two + "...")
    # notify that plot is being generated
    lin_regress = LinearRegression()
    x = dataframe[stat_one].values.reshape(-1, 1)  # set x val
    # note the reshape is necessary if only one feature
    y = dataframe[stat_two] # set y-val
    lin_regress.fit(x, y)  # Create a regression model
    lin_predict = lin_regress.predict(x)  # Predict values based on regression model
    figure = plt.figure() # create figure object
    plt.scatter(x, y, color='black')  # plot the actual data as black circles
    plt.xlabel(stat_one) # set x label
    plt.ylabel(stat_two) # set y label
    plt.title(stat_one + " versus " + stat_two) # set title
    plt.plot(x, lin_predict, 'cs')  # plot the expected results from the regression as cyan
    figure.savefig("plots/"+stat_one+"versus"+stat_two+"_lreg.png", dpi=figure.dpi) # save the figure into loc
    print("Finished. Output saved to " + "plots/"+stat_one+"versus"+stat_two+"_lreg.png") # notify that plot is created

