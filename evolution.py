import sys, os
sys.path.insert(0, "evoman")

from demo_controller import player_controller
from environment import Environment
from analyse import plot
from rank_selection import rank_selection
from mutations import uni_mutation, scramble_mutation

import crossovers
import tournaments
import time

import numpy as np
from random import randint
from tournaments import sort_population

# Parameters
BOUND_MAX = 1
BOUND_MIN = -1
ENEMY_NR = [1, 2]


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


experiment_name = "ANN1_2"

if not os.path.exists(experiment_name):
    os.makedirs(experiment_name)

env = Environment(experiment_name = experiment_name,
                  enemies = ENEMY_NR,
                  player_controller = player_controller(),
                  multiplemode = "yes")

# Multilayer with 10 hidden neurons
N_HIDDEN = 10
N_VARS = (env.get_num_sensors()+1)*N_HIDDEN + (N_HIDDEN+1)*5


def ANN_fitness(pop, popf):

    pass


def run_simulation(env, pop, nr):
    """
    Runs simulation for every individual in the population.
    """
    pop_f = []
    pop_pl = []
    pop_el = []

    for individual in pop:
        fitness, player_life, enemy_life, time = env.play(pcont=individual)
        pop_f.append(fitness)
        pop_pl.append(player_life)
        pop_el.append(enemy_life)

    return pop_f, pop_pl, pop_el


def evolution_process(N, K, num_gens, cmin, cmax, sigma, chance, selection, mutation_type):
    """
    EVOLUTION PROCESS:
    Fitness calculation > mating pool > parents selection,
    Mating (crossover and mutation) > offspring.
    """

    nr = 0

    # Start with random population
    pop = np.random.uniform(BOUND_MIN, BOUND_MAX, (N, N_VARS))
    pop_f, pop_pl, pop_el = run_simulation(env, pop, nr)

    # Keep track of max and mean fitness over generations
    f_max = []
    f_mean = []
    counter = 0

    # Obtain results for every generation
    for generation in range(num_gens):

        # +1 since begin population is generation 0
        print("GENERATION: " + str(generation + 1))

        # Start with random begin population
        if generation == 0:
            f_max.append(max(pop_f))
            f_mean.append(np.mean(pop_f))

        # Parent selection can be K-way or Rank selection
        if selection == "kway":
            parents, parents_f = tournaments.choose_parents_kway(pop, pop_f, N, K)
        else:
            parents, parents_f = rank_selection(pop, pop_f, N)

        new_pop = pop
        new_pop_f = pop_f
        new_pop_pl = pop_pl
        new_pop_el = pop_el
        new_pop_children = []

        # Choose parent pairs for tournament
        for i in range(int(N/2)):

            # Choose parents based on their fitness
            parent1, parent2 = tournaments.choose_sorted_pairs(parents, parents_f, i, N)
            i = i + 2

            # Perform crossover to get new children
            child1, child2 = crossovers.crossover(parent1, parent2, cmin, cmax)

            # Add children and parents to new population
            new_pop_children.append(child1)
            new_pop_children.append(child2)

        # Mutate children (with uni or scramble mutation) and calculate new fitness
        if mutation_type == "uni":
            new_pop_children, new_pop_children_f, new_pop_children_pl, new_pop_children_el = uni_mutation(new_pop_children, env, BOUND_MIN, BOUND_MAX)
        else:
            new_pop_children, new_pop_children_f, new_pop_children_pl, new_pop_children_el = scramble_mutation(new_pop_children, env)

        # add children to population
        new_pop = np.ndarray.tolist(new_pop) + new_pop_children
        new_pop_f = new_pop_f + new_pop_children_f
        new_pop_pl = new_pop_pl + new_pop_children_pl
        new_pop_el = new_pop_el + new_pop_children_el

        # Choose the survivors, bring pop length to N / 2
        new_pop, new_pop_f, new_pop_pl, new_pop_el = tournaments.choose_survivors(new_pop, new_pop_f, new_pop_pl, new_pop_el)

        # Only use new population if it has improved
        if max(new_pop_f) > max(pop_f):
            counter = 0
        else:
            counter += 1
        pop, pop_f, pop_pl, pop_el = new_pop, new_pop_f, new_pop_pl, new_pop_el

        print("COUNTER = ", counter)

        if counter > 5:
            f_max.append(max(pop_f))
            f_mean.append(np.mean(pop_f))
            break

        # Keep track of max and mean fitness for plot
        f_max.append(max(pop_f))
        f_mean.append(np.mean(pop_f))

        # Compute gains
        print(bcolors.WARNING + str(pop_el) + bcolors.ENDC)

        gains = []
        pl = []
        el = []
        for j in range(len(pop_pl)):
            gains.append(pop_pl[j] - pop_el[j])
            el.append(pop_el)
            pl.append(pop_pl)
        print(gains, "GAINS")
        # gains = pop_el - pop_pl
        # print(bcolors.HEADER + str(gains) + bcolors.ENDC)

    # Sort population to get individual with highest fitness
    pop_sorted, pop_f_sorted, pop_pl_sorted, pop_el_sorted = sort_population(pop, pop_f, pop_pl, pop_el)
    best_pop_f, best_pop_pl, best_pop_el = evaluate_best(env, pop_sorted[-1])

    print(bcolors.WARNING + str(best_pop_f) + bcolors.ENDC)

    # saves results for best population
    file_aux = open(experiment_name + "/results.txt", "a")
    file_aux.write(str(pop_sorted[-1]) + str(pop_f_sorted[-1]) + "\n")
    file_aux.close()

    # Save array of max values
    file_aux = open(experiment_name + "/maxvalues.txt", "a")
    file_aux.write(time.strftime("%d-%m %H:%M ", time.localtime()) + "\n" + "Max: " + str(f_max) + "\n" + "Mean: " + str(f_mean) + "\n")
    file_aux.write("Gains:" + str(gains) + "\n" + "Enemylife:" + str(pop_el) + "\n" + "Playerlife:" + str(pop_pl) + "\n")
    file_aux

    return f_max, f_mean, pop_sorted[-1], best_pop_f, best_pop_pl, best_pop_el


def evaluate_best(env, best):
    """
    Evaluate best individual.
    """

    best = np.asarray(best)
    fitness, pl, el, time = env.play(pcont=best)
    print("DIT IS EEN TEST: Fitness = ", fitness, "Player life = ", pl, "Enemy life = ", el)
    return fitness, pl, el
