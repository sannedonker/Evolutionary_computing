import sys, os
sys.path.insert(0, "evoman")

from demo_controller import player_controller
from environment import Environment
from mutations import non_uni_mutation

import crossovers
import tournaments

import numpy as np
from random import randint

# parameters
K = 3
N = 10
BOUND_MAX = 1
BOUND_MIN = -1
ENEMY_NR = [2]
NUM_GENERATIONS = 3
OFSPRING_SIZE = 10
nr_generations = 2

experiment_name = "TESTEN"
if not os.path.exists(experiment_name):
    os.makedirs(experiment_name)

env = Environment(experiment_name = experiment_name,
                  enemies = ENEMY_NR,
                  player_controller = player_controller(),
                  speed = "fastest",
                  savelogs="no")

# TODO: snappen wat en hoe
N_HIDDEN = 10
N_VARS = (env.get_num_sensors()+1)*N_HIDDEN + (N_HIDDEN+1)*5 # multilayer with 10 hidden neurons


def run_simulation(env, pop):
    pop_f = []
    pop_pl = []
    pop_el = []
    pop_t = []
    for individual in pop:
        fitness, player_life, enemy_life, time = env.play(pcont = individual)
        pop_f.append(fitness)
        pop_pl.append(player_life)
        pop_el.append(enemy_life)
        pop_t.append(time)

    return pop_f, pop_pl, pop_el, pop_t

# TODO
# eventjes dit zodat die niet godverdomme de hele tijd alles moet doorlopen
# wel best wat dingen gekopieerd van haar dus moeten we nog wel echt even eigen maken
if not os.path.exists(experiment_name+'/results.txt'):

    # beginpop and corresponding data
    beginpop = np.random.uniform(BOUND_MIN, BOUND_MAX, (N, N_VARS))
    beginpop_f = run_simulation(env, beginpop)[0]
    best_f = max(beginpop_f)
    best_position = beginpop_f.index(max(beginpop_f))
    average = np.mean(beginpop_f)
    std = np.std(beginpop_f)

    # saves results for begin population
    file_aux  = open(experiment_name + "/results.txt", "a")
    file_aux.write(str(beginpop[best_position]) + str(beginpop_f[best_position]))
    file_aux.close()

    solutions = [beginpop, beginpop_f]
    env.update_solutions(solutions)
    env.save_state()

else:
    env.load_state()
    beginpop = env.solutions[0]
    beginpop_f = env.solutions[1]


# evolution process
def evolution_process(nr_generations, beginpop, beginpop_f):
    """
    EVOLUTION PROCESS:
    Fitness calculation > mating pool > parents selection,
    Mating (crossover and mutation) > offspring.
    """

    for i in range(nr_generations):

        # Start with random begin population
        if i == 0:
            pop, pop_f = beginpop, beginpop_f

        parents = tournaments.choose_parents_kway(pop, pop_f, N, K)

        new_pop = []

        # Choose parent pairs for tournament
        for i in range(int(N/2)):

            # TODO: bedenken hoe we de ouder-paren willen bepalen
            # Nu is het alleen steeds [ouder1 + ouder2, ouder2 + ouder3...]
            parent1, parent2 = tournaments.choose_pairs(parents, i)
            i = i + 2

            # Perform crossover to get new children
            child1, child2 = crossovers.crossover(parent1, parent2)

            # Add children and parents to new population
            new_pop.append(parent1)
            new_pop.append(parent2)
            new_pop.append(child1)
            new_pop.append(child2)

        # Take half of population
        # cut = int(0.5 * len(new_pop))
        # new_pop = new_pop[:cut]
        tournaments.choose_survivors(beginpop, beginpop_f)


        # Mutate children
        pop, pop_f = non_uni_mutation(new_pop, env)
        print(len(pop), "LENGTH NEW POP")

        solutions = [pop, pop_f]
        env.update_solutions(solutions)
        env.save_state()
    # exit()

evolution_process(nr_generations, beginpop, beginpop_f)
