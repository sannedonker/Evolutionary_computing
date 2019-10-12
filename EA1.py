import sys, os
from evolution import evolution_process
import matplotlib.pyplot as plt
import numpy as np
import time

# Parameters
N = 10
K = [3]
NUM_GENERATIONS = 15
CROSSOVER_MIN = 0.5
CROSSOVER_MAX = 0.9
MUTATION_SIGMA = 0.5
MUTATION_CHANCE = 0.15
RUNS = 1


experiment_name = "ANN1_"


if __name__ == "__main__":

    # Determine K
    for i in range(RUNS):
        parent_select_type = "kway"
        mutation_type = "uni"

        for j in K:
            if not os.path.exists(experiment_name + str(j)):
                os.makedirs(experiment_name + str(j))

            f_max, f_mean, pop_sorted, best_pop_f, best_pop_pl, best_pop_el = evolution_process(N, j,
                             NUM_GENERATIONS,
                             CROSSOVER_MIN, CROSSOVER_MAX,
                             MUTATION_SIGMA, MUTATION_CHANCE,
                             parent_select_type, mutation_type)

            # Saves results for best population
            # List with best individual and tuple with all it's information
            file_aux = open(experiment_name + str(j) + "/results.txt", "a")
            file_aux.write(str(pop_sorted) + str(best_pop_f) + str(best_pop_pl) + str(best_pop_el) + "\n")
            file_aux.close()

            # Save array of max values
            # length of mean and max is number of generations (incl gen 0)
            file_aux = open(experiment_name + str(j) + "/maxvalues.txt", "a")
            file_aux.write(time.strftime("%d-%m %H:%M ", time.localtime()) + "\n" + "Best fitness: " + str(best_pop_f) +  "\n")
            file_aux.write("Enemylife:" + str(best_pop_el) + "\n" + "Playerlife:" + str(best_pop_pl) + "\n")
            file_aux.close()
