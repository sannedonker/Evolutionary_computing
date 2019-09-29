import sys, os
sys.path.insert(0, "evoman")

from demo_controller import player_controller
from environment import Environment
from mutations import non_uni_mutation, uni_mutation, scramble_mutation
from analyse import plot
from rank_selection import rank_selection

import crossovers
import tournaments
import time

import numpy as np
from random import randint
from tournaments import sort_population

BOUND_MAX = 1
BOUND_MIN = -1
ENEMY_NR = [3]
#nr_generations = 2

experiment_name = "EA2_results"
if not os.path.exists(experiment_name):
    os.makedirs(experiment_name)

env = Environment(experiment_name = experiment_name,
                  enemies = ENEMY_NR,
                  player_controller = player_controller(),
                  # speed = "fastest",
                  savelogs="no")

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


# evolution process
def evolution_process(N, K, num_gens, cmin, cmax, sigma, chance, method, selection, mutation_type):
    """
    EVOLUTION PROCESS:
    Fitness calculation > mating pool > parents selection,
    Mating (crossover and mutation) > offspring.
    """

    # Start with random population
    beginpop = np.random.uniform(BOUND_MIN, BOUND_MAX, (N, N_VARS))
    beginpop_f = run_simulation(env, beginpop)[0]

    # Keep track of max and mean fitness over generations
    f_max = []
    f_mean = []

    for i in range(num_gens):

        # Start with random begin population
        if i == 0:
            pop, pop_f = beginpop, beginpop_f

            f_max.append(max(pop_f))
            f_mean.append(np.mean(pop_f))
            parents, parents_f = pop, pop_f
        else:
            if selection == "kway":
                parents, parents_f = tournaments.choose_parents_kway(pop, pop_f, N, K)
            else:
                parents, parents_f = rank_selection(pop, pop_f, N)

        new_pop = []

        # TODO: dit gaat nu best omslachtig, misschien meer in de choose pairs
        # functies zetten???
        # Choose parent pairs for tournament
        for i in range(int(N/2)):

            # Choose parents based on their fitness
            parent1, parent2 = tournaments.choose_sorted_pairs(parents, parents_f, i, N)
            i = i + 2

            # Perform crossover to get new children
            child1, child2 = crossovers.crossover(parent1, parent2, cmin, cmax)

            # Add children and parents to new population
            new_pop.append(parent1)
            new_pop.append(parent2)
            new_pop.append(child1)
            new_pop.append(child2)

        # Mutate children and calculate new fitness
        if mutation_type == "uni":
            pop, pop_f = non_uni_mutation(new_pop, env, BOUND_MIN, BOUND_MAX, sigma, chance)
        else:
            pop, pop_f = scramble_mutation(new_pop, env)


        # Choose the survivors, bring pop length back from 20 to 10
        pop, pop_f = tournaments.choose_survivors(pop, pop_f)

        solutions = [pop, pop_f]
        env.update_solutions(solutions)

        # keep track of max and mean fitness for plot
        f_max.append(max(pop_f))
        f_mean.append(np.mean(pop_f))


        print("Max: ", f_max, ", Mean: ", f_mean)

    # plot figure with max and mean fitness over generations
    # plot(num_gens, f_max, f_mean)

    # Sort population to get individual with highest fitness
    pop_sorted, pop_f_sorted = sort_population(pop, pop_f)

    # saves results for begin population
    file_aux  = open(experiment_name + "/results.txt", "a")
    file_aux.write(str(pop_sorted[-1]) + str(pop_f_sorted[-1]) + "\n")
    file_aux.close()

    # Save array of max values
    file_aux  = open(experiment_name + "/maxvalues.txt", "a")
    file_aux.write(time.strftime("%d-%m %H:%M ", time.localtime()) + "Max: " + str(f_max) + " Mean: " + str(f_mean) + "\n")
    # file_aux.close()
    return f_max, f_mean
