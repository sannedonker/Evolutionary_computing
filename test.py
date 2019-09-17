import sys, os
sys.path.insert(0, "evoman")

from demo_controller import player_controller
from environment import Environment

import numpy as np

# parameters
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
# tournament parents
# crossover
# mutatie
# tournament surviving

# beginpop and corresponding data
beginpop = np.random.uniform(BOUND_MIN, BOUND_MAX, (N, N_VARS))
beginpop_f = run_simulation(env, beginpop)[0]
best_f = max(beginpop_f)
best_position = beginpop_f.index(max(beginpop_f))
average = np.mean(beginpop_f)
std = np.std(beginpop_f)

# saves results for begin population
file_aux  = open(experiment_name + "/results.txt", "a")
file_aux.write(str(beginpop[best_position]) + " " + str(beginpop_f[best_position]))
file_aux.close()

# evolution process
def choosing_parents_kway(pop, pop_f):
    """
    Choose parents with a K-way tournament
    Input: population, number of contestents: K
    Output: list of parents
    """
    parents = []
    for i in range(N):

        # choose K individuals that will enter the tournament
        battlefield = []
        for j in range(K):

            # choose random individual, remove from population, add to battlefield
            chosen = random.choice(pop)
            index = pop.index(chosen)
            fitness = pop_f[index]
            pop.remove(chosen)
            pop_f.remove(fitness)
            battlefield.append((chosen, fitness))

        # choose winner, add winner to the parents
        winner = sorted(battlefield, key=itemgetter(1))[-1][0]
        parents.append(winner)

        # put contestents and corresponding fitness back in the population
        for j in range(K):
            pop.append(battlefield[j][0])
            pop_f.append(battlefield[j][1])

    print(parents)
    return parents

# choosing_parents_kway(beginpop, beginpop_f)
