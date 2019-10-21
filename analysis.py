import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
sns.set()

gains = []
maxes = []
enemylifes = []
pllifes = []


def get_means(var):
    temp = [np.mean([x[i] for x in var if len(x) > i]) for i in range(len(max(var, key=len)))]
    return temp


def stripper(line, category):

    if category in line:

        values = []
        lines = line.strip(category)

        lines = lines.split(",")
        for value in lines:

            temp = value.strip(" [")
            temp = temp.strip("[")
            temp = temp.strip("]\n")
            values.append(float(temp) + 10)

        if category == "Gains:":
            gains.append(values)
        elif category == "Max: ":
            maxes.append(values)
        elif category == "Enemylife:":
            enemylifes.append(values)
        elif category == "Playerlife:":
            pllifes.append(values)

    return gains, maxes, enemylifes, pllifes


def load_file():

    with open("EA1_[1, 2, 3, 4, 5, 6, 7, 8]/maxvalues.txt", "r") as f:

        for line in f:

            gains = stripper(line, "Gains:")[0]
            maxes = stripper(line, "Max: ")[1]
            enemylifes = stripper(line, "Enemylife:")[2]
            pllifes = stripper(line, "Playerlife:")[3]

    return gains, maxes, enemylifes, pllifes


gains, maxes, enemylifes, pllifes = load_file()

# print(gains)
mean_gains = get_means(gains)
mean_maxs = get_means(maxes)
enemylifes_means = get_means(enemylifes)
pllifes_means = get_means(pllifes)

plt.ylabel("Gains")
plt.xlabel("Generations")
plt.plot(mean_gains)
plt.show()

plt.ylabel("Max fitness")
plt.xlabel("Generations")
plt.plot(mean_maxs)
plt.show()

plt.ylabel("Life")
plt.xlabel("Generations")
plt.plot(enemylifes_means)
plt.plot(pllifes_means)
plt.plot(mean_gains)
plt.legend(["Ememy life", "Player life", "Gains"])
plt.show()
