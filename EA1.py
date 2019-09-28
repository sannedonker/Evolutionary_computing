from evolution import evolution_process

# parameters
N = 2 # MUST BE AN EVEN NUMBER
K = 1
NUM_GENERATIONS = 1
CROSSOVER_MIN = 0.5
CROSSOVER_MAX = 0.9
MUTATION_SIGMA = 0.5
MUTATION_CHANCE = 0.15
MUTATION_METHOD = 1


if __name__ == "__main__":

    evolution_process(N, K, NUM_GENERATIONS,
                     CROSSOVER_MIN, CROSSOVER_MAX,
                     MUTATION_SIGMA, MUTATION_CHANCE,
                     MUTATION_METHOD)
