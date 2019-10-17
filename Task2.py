import sys, os
from evolution import evolution_process, test_for_all
import matplotlib.pyplot as plt
import numpy as np
import time

# Parameters
N = 100
K = 20
NUM_GENERATIONS = 15
CROSSOVER_MIN = 0.5
CROSSOVER_MAX = 0.9
MUTATION_SIGMA = 0.5
MUTATION_CHANCE = 0.15
parent_select_type = "kway"
mutation_type = "scramble"
RUNS = 10
ENEMIES = [[1, 2, 3, 4, 5, 6, 7, 8]]

# ______TESTING PARAMETERS_______
# N = 4
# K = 2
# NUM_GENERATIONS = 1
# CROSSOVER_MIN = 0.5
# CROSSOVER_MAX = 0.9
# MUTATION_SIGMA = 0.5
# MUTATION_CHANCE = 0.15
# parent_select_type = "kway"
# mutation_type = "uni"
# RUNS = 1


# experiment_name = "ENEMY_COMBINATION_"

if __name__ == "__main__":

    for enemy in ENEMIES:

        experiment_name = "EA2_" + str(enemy)

        for i in range(RUNS):

            if not os.path.exists(experiment_name):
                os.makedirs(experiment_name)

            f_max, f_mean, best_pop, best_pop_f, best_pop_pl, best_pop_el = evolution_process(
                 N, K, NUM_GENERATIONS, CROSSOVER_MIN, CROSSOVER_MAX,
                 MUTATION_SIGMA, MUTATION_CHANCE,
                 parent_select_type, mutation_type, enemy)

            file_aux = open(experiment_name + "/results.txt", "a")
            file_aux.write(str(enemy) + "\n" + str(best_pop) + "best fitness:" + str(best_pop_f) + "player life:" + str(best_pop_pl) + "enemy life:" + str(best_pop_el) + "\n")
            file_aux.close()

            file_aux = open(experiment_name + "/maxvalues.txt", "a")
            file_aux.write("\n"+ str(enemy) + "\n" + "BEST fitness: " + str(best_pop_f) +  "\n")
            file_aux.write("Enemylife: " + str(best_pop_el) + "\n" + "Playerlife: " + str(best_pop_pl) + "\n")
            file_aux.write("\n")
            file_aux.close()

            test_for_all(best_pop, experiment_name)
