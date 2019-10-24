import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
sns.set()

def get_means(var):
    temp = [np.mean([x[i] for x in var if len(x) > i]) for i in range(len(max(var, key=len)))]
    return temp


def stripper(total, line, category):

    gains, maxes, enemylifes, pllifes = total[0], total[1], total[2], total[3]
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


def load_file(EA):

    gains = []
    maxes = []
    enemylifes = []
    pllifes = []
    total = [gains, maxes, enemylifes, pllifes]

    with open(f"EA{EA}_ALLVALUES[1, 2, 3, 4, 5, 6, 7, 8]/maxvalues.txt", "r") as f:

        for line in f:

            gains = stripper(total, line, "Gains:")[0]
            maxes = stripper(total, line, "Max: ")[1]
            enemylifes = stripper(total, line, "Enemylife:")[2]
            pllifes = stripper(total, line, "Playerlife:")[3]

    return gains, maxes, enemylifes, pllifes


gains, maxes, enemylifes, pllifes = load_file(1)
gains2, maxes2, enemylifes2, pllifes2 = load_file(2)

# print(gains)
mean_gains = get_means(gains)
mean_maxs = get_means(maxes)
enemylifes_means = get_means(enemylifes)
pllifes_means = get_means(pllifes)

mean_gains2 = get_means(gains2)
mean_maxs2 = get_means(maxes2)
enemylifes_means2 = get_means(enemylifes2)
pllifes_means2 = get_means(pllifes2)

print(mean_gains)
print(mean_gains2)
plt.ylabel("Gains")
plt.xlabel("Generations")
plt.plot(mean_gains)
plt.plot(mean_gains2)
plt.show()

plt.ylabel("Max fitness")
plt.xlabel("Generations")
plt.plot(mean_maxs)
plt.plot(mean_maxs2)
plt.show()

plt.ylabel("Life")
plt.xlabel("Generations")
plt.plot(enemylifes_means)
plt.plot(enemylifes_means2)
plt.plot(pllifes_means)
plt.plot(pllifes_means2)
plt.plot(mean_gains)
plt.plot(mean_gains2)
plt.legend(["Ememy life EA1", "Ememy life EA2", "Player life EA1", "Player life EA2", "Gains EA1", "Gains EA2"])
plt.show()
