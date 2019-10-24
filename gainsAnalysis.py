import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
import sys, os
from evolution import final_test, test_for_all_list, evolution_process
sns.set()

maxes = []
enemylifes = []
pllifes = []
ENEMIES = [1, 2, 3, 4, 5, 6, 7, 8]


def load_sol_list(EA):

    sol_list = []

    with open(f"EA{EA}_ALLVALUES/results.txt", "r") as f:

        for line in f:
            beginpop = []

            line = line.split(",")
            for value in line:

                temp = value.strip(" [")
                temp = temp.strip("[")
                temp = temp.strip(" ")
                temp = temp.strip("]\n")

                try:
                    beginpop.append(float(temp))
                except ValueError:
                    beginpop = []

            sol_list.append(beginpop)

    return sol_list


def get_means(var):
    temp = [np.mean([x[i] for x in var if len(x) > i]) for i in range(len(max(var, key=len)))]
    return temp


# Load solutions of one EA
# solutions = load_sol_list(1)
#
# # Test every solution from every run (10 solutions):
# # This is repeated 5 times for every solution
# total_solutions_all_enemies = []
# for solution in solutions:
#     enemy_sol = test_for_all_list(solution)
#
#     total_solutions_all_enemies.append(enemy_sol)

# total_solutions_all_enemies contains information of gains for 5 runs on
# all enemies testes with the best 10 solutions (10 runs)
# print(total_solutions_all_enemies)

total_solutions_all_enemies1 = [[-60.0, 24.0, -40.0, -40.0, 49.60000000000031, -20.0, -10.0, 22.600000000000243], [-50.0, 52.0, 18.0, -50.0, 43.00000000000029, -50.0, -10.0, -50.0], [-50.0, 56.0, -40.0, -40.0, 49.60000000000031, -20.0, -20.0, 4.0000000000002345], [-60.0, 74.0, 4.0, -70.0, 56.20000000000032, -60.0, 59.80000000000033, 16.000000000000227], [-40.0, 74.0, -40.0, -60.0, 55.00000000000032, -20.0, -10.0, -30.0], [-50.0, -20.0, -30.0, -30.0, 52.600000000000314, -80.0, -10.0, -30.0], [-40.0, 76.0, -20.0, -0.5999999999997687, 53.80000000000032, -80.0, 51.40000000000031, 8.200000000000232], [-70.0, -40.0, -50.0, -40.0, 28.000000000000256, -30.0, -30.0, -70.0], [-60.0, 74.0, 2.0, -70.0, 58.00000000000033, -30.0, -10.0, 1.6000000000002341], [-70.0, 78.0, -30.0, -40.0, 50.20000000000031, -40.0, -10.0, 22.600000000000243], [-100.0, -100.0, -100.0, -100.0, -43.79999999999968, -100.0, -100.0, -100.0]]
total_solutions_all_enemies2 = [[-70.0, 74.0, -20.0, -60.0, 55.60000000000032, -30.0, 68.2000000000003, -20.0], [-70.0, 70.0, -30.0, -40.0, 60.40000000000033, -20.0, -10.0, -20.0], [-70.0, 72.0, -30.0, -40.0, 44.200000000000294, -20.0, -10.0, 48.400000000000304], [-40.0, 74.0, 4.0, -60.0, 59.20000000000033, -80.0, -20.0, -20.0], [-20.0, 86.0, 12.0, -60.0, 48.400000000000304, -80.0, 59.80000000000033, -20.0], [-80.0, 52.0, -30.0, -30.0, 41.80000000000029, -30.0, -20.0, -30.0], [-80.0, 76.0, -20.0, -30.0, 46.6000000000003, -60.0, -10.0, 22.600000000000243], [-70.0, 74.0, -10.0, -70.0, 53.200000000000315, -80.0, -10.0, 2.200000000000234], [-60.0, 28.0, -30.0, -30.0, 31.000000000000263, -20.0, -20.0, 8.800000000000232], [-90.0, -40.0, -70.0, -60.0, 29.80000000000026, -30.0, -30.0, 21.40000000000024]]


plotgainsmeans1, plotgainsmeans2 = [], []


for sol in total_solutions_all_enemies1:
    print(sol)
    plotgainsmeans1.append(np.mean(sol))

for sol in total_solutions_all_enemies2:
    plotgainsmeans2.append(np.mean(sol))

print(len(plotgainsmeans1), len(plotgainsmeans2))

plt.ylabel("Gains")
plt.boxplot([plotgainsmeans1, plotgainsmeans2])
plt.xticks([1, 2], ["EA1", "EA2"])
plt.show()
