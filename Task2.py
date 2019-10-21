import sys, os
from evolution import final_test, test_for_all, evolution_process
import matplotlib.pyplot as plt
import numpy as np
import time

# Parameters
N = 60
K = 20
NUM_GENERATIONS = 15
CROSSOVER_MIN = 0.5
CROSSOVER_MAX = 0.9
MUTATION_SIGMA = 0.5
MUTATION_CHANCE = 0.15
parent_select_type = "kway"
mutation_type = "uni"
RUNS = 10
enemy = [1, 2, 3, 4, 5, 6, 7, 8]


# ______TESTING PARAMETERS_______
# N = 2
# K = 2
# NUM_GENERATIONS = 3
# CROSSOVER_MIN = 0.5
# CROSSOVER_MAX = 0.9
# MUTATION_SIGMA = 0.5
# MUTATION_CHANCE = 0.15
# parent_select_type = "kway"
# mutation_type = "uni"
# RUNS = 1
# ENEMIES = [1, 2, 3, 4, 5, 6, 7, 8]


# experiment_name = "ENEMY_COMBINATION_"

# Experiment
if __name__ == "__main__":

    experiment_name = "EA1_ALLVALUES" + str(enemy)
    if not os.path.exists(experiment_name):
        os.makedirs(experiment_name)

    for i in range(RUNS):

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
    #
    # for enemy in ENEMIES:
    #
    #     for nr, beginpop in enumerate(bsols):
    #
    #         experiment_name = "FINAL_ENEMY_" + str(enemy) + "_SOL_" + nr
    #
    #         for i in range(RUNS):
    #
    #             if not os.path.exists(experiment_name):
    #                 os.makedirs(experiment_name)
    #
    #             pop, pop_f, pop_pl, pop_el, gains = final_test(beginpop, enemy)
    #
    #             file_aux = open(experiment_name + "/results.txt", "a")
    #             file_aux.write(str(pop) + "fitness:" + str(pop_f) + "player life:" + str(pop_pl) + "enemy life:" + str(pop_el) + "\n")
    #             file_aux.close()
    #
    #             file_aux = open(experiment_name + "/maxvalues.txt", "a")
    #             file_aux.write("BEST fitness: " + str(pop_f) +  "Gains: " + str(gains) + "\n")
    #             file_aux.write("Enemylife: " + str(pop_el) + "\n" + "Playerlife: " + str(pop_pl) + "\n")
    #             file_aux.write("\n")
    #             file_aux.close()
    #
    #             # test_for_all(best_pop, experiment_name)
