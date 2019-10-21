import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
sns.set()

maxes = []
enemylifes = []
pllifes = []
plotgains = []


def get_means(var):
    temp = [np.mean([x[i] for x in var if len(x) > i]) for i in range(len(max(var, key=len)))]
    return temp


def stripper(gains, line, category):

    if category in line:
        values = []
        lines = line.strip(category)

        lines = lines.split(",")
        for value in lines:

            temp = value.strip(" [")
            temp = temp.strip("[")
            temp = temp.strip(" ")
            temp = temp.strip("]\n")
            values.append(float(temp))

        if category == "Gains:":
            gains.append(values[0])
        elif category == "Max: ":
            maxes.append(values)
        elif category == "Enemylife:":
            enemylifes.append(values)
        elif category == "Playerlife:":
            pllifes.append(values)

    return gains, maxes, enemylifes, pllifes


def load_file(nr):

    gains = []

    with open(f"FINAL_ENEMY_{nr}/maxvalues.txt", "r") as f:

        for line in f:

            gains = stripper(gains, line, "Gains:")[0]


    return gains


# gains, maxes, enemylifes, pllifes = load_file()

for i in range(1, 8 + 1):
    print(i)
    gains = load_file(i)
    plotgains.append(gains)

df = pd.DataFrame(plotgains)

plt.xlabel("Enemy number")
plt.ylabel("Gains")
plt.boxplot(df)
plt.show()
# print(plotgains)
# plt.boxplot(gains)
