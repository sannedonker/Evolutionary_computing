from evolution import evolution_process

if __name__ == "__main__":

    # Times to run complete algorithm (to plot average of average)
    # for i in range(3):


    evolution_process(N = 6,
                      K = 3,
                      num_gens = 4,
                      cmin = 0.5,   # crossover chance min
                      cmax = 0.9,   # crossover chance max
                      sigma = 0.6,  # uni mutation
                      chance = 0.1, # uni mutation
                      selection="rank",
                      mutation_type="scramble")
