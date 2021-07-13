from matplotlib import pyplot as plt

WEAK_THRESHOLD = 200
MOD_THRESHOLD = 400


def power(row):
    if row["Total"] < WEAK_THRESHOLD:
        return "weak"
    elif row["Total"] < MOD_THRESHOLD:
        return "moderate"
    else:
        return "strong"


def create_power_histogram(dataframe):
    print("Generating power histogram...")
    # notify that plot is being generated
    dataframe["Power"] = dataframe.apply(power, axis=1)
    figure = plt.figure()
    plt.hist([dataframe["Power"]], bins=7, )
    plt.xlabel("Power")
    plt.title("Power Histogram")
    figure.savefig("plots/power_histogram.png", dpi=figure.dpi)
    print("Finished. Output saved to plots/power_histogram.png.")  # notify that plot is created
