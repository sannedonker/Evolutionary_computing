import sys, os

from evolution import evolution_process
import matplotlib.pyplot as plt
import numpy as np

import time

# parameters
N = 100 # MUST BE AN EVEN NUMBER
K = [5]
NUM_GENERATIONS = 15
CROSSOVER_MIN = 0.5
CROSSOVER_MAX = 0.9
MUTATION_SIGMA = 0.5
MUTATION_CHANCE = 0.15
RUNS = 10

experiment_name = "EA2_ENEMY2_"


if __name__ == "__main__":

    # DETERMINE K
    for i in range(RUNS):
        parent_select_type = "kway"
        mutation_type = "scramble"

        # for parent_select_type in parent_select_types:
        for j in K:

            if not os.path.exists(experiment_name + str(j)):
                os.makedirs(experiment_name + str(j))

            f_max, f_mean, pop_sorted, best_pop_info = evolution_process(N, j,
                             NUM_GENERATIONS,
                             CROSSOVER_MIN, CROSSOVER_MAX,
                             MUTATION_SIGMA, MUTATION_CHANCE,
                             parent_select_type, mutation_type)

            # saves results for best population
            # list with best individual and tuple with all it's information
            file_aux  = open(experiment_name + str(j) + "/results.txt", "a")
            file_aux.write(str(pop_sorted) + str(best_pop_info) + "\n")
            file_aux.close()

            # Save array of max values
            # length of mean and max is number of generations (incl gen 0)
            file_aux  = open(experiment_name + str(j) + "/maxvalues.txt", "a")
            file_aux.write(time.strftime("%d-%m %H:%M ", time.localtime()) + "Max: " + str(f_max) + " Mean: " + str(f_mean) + "\n")
            # file_aux.close()




    # for parent_select_type in parent_select_types:
    # for mutation_type in mutation_types:
    #     f_max, f_mean = evolution_process(N, K, NUM_GENERATIONS,
    #                      CROSSOVER_MIN, CROSSOVER_MAX,
    #                      MUTATION_SIGMA, MUTATION_CHANCE,
    #                      parent_select_type, mutation_type)
    #     plt.plot(list(range(0, NUM_GENERATIONS + 1)), f_max, label = 'best ' + mutation_type)
    #     plt.plot(list(range(0, NUM_GENERATIONS + 1)), f_mean, label = 'mean ' + mutation_type)
    #
    # # plt.title('K-way VS Rank selection')
    # plt.title('Uni VS Scramble mutation')
    # plt.xlabel(xlabel = 'Generation number')
    # plt.ylabel(ylabel = 'Fitness')
    # plt.legend()
    # plt.show()
