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

experiment_name = "TESTEN"
if not os.path.exists(experiment_name):
    os.makedirs(experiment_name)

env = Environment(experiment_name = experiment_name,
                  enemies = ENEMY_NR,
                  player_controller = player_controller())

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
# tournaments.choose_parents_kway(beginpop, beginpop_f, N, K)
# crossovers.crossover(beginpop[0], beginpop[1])
#non_uni_mutation(beginpop, env)
