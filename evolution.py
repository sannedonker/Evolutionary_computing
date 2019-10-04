import sys, os
sys.path.insert(0, "evoman")

from demo_controller import player_controller
from environment import Environment
from mutations import *
from analyse import plot
from rank_selection import rank_selection

import crossovers
import mutations
import tournaments
import time

import numpy as np
from random import randint
from tournaments import sort_population

# Parameters
BOUND_MAX = 1
BOUND_MIN = -1
ENEMY_NR = [4]


experiment_name = "EA1_results_EN4_"

if not os.path.exists(experiment_name):
    os.makedirs(experiment_name)

env = Environment(experiment_name = experiment_name,
                  enemies = ENEMY_NR,
                  player_controller = player_controller(),
                  level = 2,
                  contacthurt = "player",
                  savelogs="no")

# Multilayer with 10 hidden neurons
N_HIDDEN = 10
N_VARS = (env.get_num_sensors()+1)*N_HIDDEN + (N_HIDDEN+1)*5


def run_simulation(env, pop):
    """
    Runs simulation for every individual in the population.
    """
    pop_f = []
    pop_pl = []
    pop_el = []
    pop_t = []

    for individual in pop:
        fitness, player_life, enemy_life, time = env.play(pcont=individual)
        pop_f.append(fitness)
        pop_pl.append(player_life)
        pop_el.append(enemy_life)
        pop_t.append(time)

    return pop_f, pop_pl, pop_el, pop_t


def evolution_process(N, K, num_gens, cmin, cmax, sigma, chance, selection, mutation_type):
    """
    EVOLUTION PROCESS:
    Fitness calculation > mating pool > parents selection,
    Mating (crossover and mutation) > offspring.
    """

    # Start with random population
    pop = np.random.uniform(BOUND_MIN, BOUND_MAX, (N, N_VARS))
    pop_f = run_simulation(env, pop)[0]

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
            new_pop_children, new_pop_children_f = uni_mutation(new_pop_children, env, BOUND_MIN, BOUND_MAX)
        else:
            new_pop_children, new_pop_children_f = scramble_mutation(new_pop_children, env)

        # add children to population
        new_pop = np.ndarray.tolist(new_pop) + new_pop_children
        new_pop_f = new_pop_f + new_pop_children_f

        # Choose the survivors, bring pop length to N / 2
        new_pop, new_pop_f = tournaments.choose_survivors(new_pop, new_pop_f)

        # Only use new population if it has improved
        if max(new_pop_f) > max(pop_f):
            counter = 0
        else:
            counter += 1
        pop, pop_f = new_pop, new_pop_f

        print("COUNTER = ", counter)

        if counter > 5:
            f_max.append(max(pop_f))
            f_mean.append(np.mean(pop_f))
            break

        # Keep track of max and mean fitness for plot
        f_max.append(max(pop_f))
        f_mean.append(np.mean(pop_f))

    # Sort population to get individual with highest fitness
    pop_sorted, pop_f_sorted = sort_population(pop, pop_f)
    best_pop_info = evaluate_best(env, pop_sorted[-1])

    # saves results for best population
    file_aux = open(experiment_name + "/results.txt", "a")
    file_aux.write(str(pop_sorted[-1]) + str(pop_f_sorted[-1]) + "\n")
    file_aux.close()

    # Save array of max values
    file_aux  = open(experiment_name + "/maxvalues.txt", "a")
    file_aux.write(time.strftime("%d-%m %H:%M ", time.localtime()) + "Max: " + str(f_max) + " Mean: " + str(f_mean) + "\n")

    return f_max, f_mean, pop_sorted[-1], best_pop_info


def evaluate_best(env, best):
    """
    Evaluate best individual.
    """
    # pop_f = []

    best = np.asarray(best)
    fitness = env.play(pcont = best)
    # pop_pl.append(player_life)
    # pop_el.append(enemy_life)
    # pop_t.append(time)

    return fitness
