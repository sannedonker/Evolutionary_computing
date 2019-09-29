from evolution import evolution_process
import matplotlib.pyplot as plt
import numpy as np

# parameters
N = 20 # MUST BE AN EVEN NUMBER
K = 3
NUM_GENERATIONS = 10
CROSSOVER_MIN = 0.5
CROSSOVER_MAX = 0.9
MUTATION_SIGMA = 0.5
MUTATION_CHANCE = 0.15
MUTATION_METHOD = 1


if __name__ == "__main__":

    # parent_select_type = input("Parent selection (kway/rank): ")
    parent_select_types = ["kway", "rank"]
    parent_select_type = "kway"
    mutation_types = ["uni", "scramble"]
    # for parent_select_type in parent_select_types:
    for mutation_type in mutation_types:
        f_max, f_mean = evolution_process(N, K, NUM_GENERATIONS,
                         CROSSOVER_MIN, CROSSOVER_MAX,
                         MUTATION_SIGMA, MUTATION_CHANCE,
                         MUTATION_METHOD, parent_select_type, mutation_type)
        plt.plot(list(range(0, NUM_GENERATIONS + 1)), f_max, label = 'best ' + mutation_type)
        plt.plot(list(range(0, NUM_GENERATIONS + 1)), f_mean, label = 'mean ' + mutation_type)
    # plt.title('K-way VS Rank selection')
    plt.title('Uni VS Scramble mutation')
    plt.xlabel(xlabel = 'Generation number')
    plt.ylabel(ylabel = 'Fitness')
    plt.legend()
    plt.show()
