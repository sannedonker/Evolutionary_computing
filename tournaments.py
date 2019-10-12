import numpy as np
import random

CONVERGENCE = 3
KEEP_PERCENTAGE = 10
KILL_PART = 4


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def sort_population(pop, pop_f, pop_pl, pop_el):
    """
    Sort population from worst to best based on fitness
    """

    sorting = np.asarray(pop_f).argsort()
    sorted_pop = np.asarray(pop)[sorting]
    sorted_f = np.asarray(pop_f)[sorting]
    sorted_pop = np.ndarray.tolist(sorted_pop)
    sorted_f = np.ndarray.tolist(sorted_f)

    if pop_pl is not None:
        sorted_pl = np.asarray(pop_pl)[sorting]
        sorted_el = np.asarray(pop_el)[sorting]
        sorted_pl = np.ndarray.tolist(sorted_pl)
        sorted_el = np.ndarray.tolist(sorted_el)
        return sorted_pop, sorted_f, sorted_pl, sorted_el
    else:
        return sorted_pop, sorted_f


def choose_parents_kway(pop, pop_f, n, k):
    """
    Choose which individuals become parents with a K-way tournament
    Input: population, number of contestents: K
    Output: list of parents
    """

    parents = []
    parents_f = []
    for i in range(n):

        # Choose K individuals that will enter the tournament
        tournament = []
        tournament_f = []
        contestents = []

        for j in range(k):
            # make sure every individual can only compete once per tournament
            contestent = random.randint(0, n - 1)
            while contestent in contestents:
                contestent = random.randint(0, n - 1)
            contestents.append(contestent)

        # Contestents is an array of random numbers between 0 and n-1
        for m in contestents:
            tournament.append(pop[m])
            tournament_f.append(pop_f[m])

        winner = tournament_f.index(max(tournament_f))
        parents.append(tournament[winner])
        parents_f.append(tournament_f[winner])

    return parents, parents_f


def choose_survivors(pop, pop_f, pop_pl, pop_el):
    """"
    First kill the worst quarter of the generation.
    Then kill a random quarter of the generation.
    """

    # Sort pop_f and then sort pop similarly
    sorted_pop, sorted_f, sorted_pl, sorted_el = sort_population(pop, pop_f, pop_pl, pop_el)

    # Always keep best KEEP_PERCENTAGE percent of population
    top = int(len(pop) / KEEP_PERCENTAGE)
    must_survive = sorted_pop[(len(pop) - top):]
    # must_survive_f = sorted_f[(len(pop) - top):]

    # Kill worst part
    quarter = int(len(pop) / KILL_PART)
    survivors = sorted_pop[quarter:]
    survivor_fitness = sorted_f[quarter:]
    survivor_pl = sorted_pl[quarter:]
    survivor_el = sorted_el[quarter:]

    # Kill a random quarter
    for i in range(quarter):
        kill = random.randint(0, len(survivors) - 1)

        # Make sure the best individuals survive, when population converges kill anyway
        i = 0
        while survivors[kill] in must_survive and i < CONVERGENCE:
            kill = random.randint(0, len(survivors) - 1)
            i += 1

        survivors.remove(survivors[kill])
        survivor_fitness.remove(survivor_fitness[kill])
        survivor_pl.remove(survivor_pl[kill])
        survivor_el.remove(survivor_el[kill])

    # If less than half of the population is killed, kill more individuals
    while len(pop) / 2 != len(survivors):
        kill = random.randint(0, len(survivors) - 1)
        survivors.remove(survivors[kill])
        survivor_fitness.remove(survivor_fitness[kill])
        survivor_pl.remove(survivor_pl[kill])
        survivor_el.remove(survivor_el[kill])

    survivors = np.array(survivors)

    return survivors, survivor_fitness, survivor_pl, survivor_el


def choose_sorted_pairs(parents, parents_f, i, pop_size):
    """
    Let the parents mate based on fitness
    Worst parent mates with best parent
    """

    parents, parents_f = sort_population(parents, parents_f, None, None)
    parents = np.array(parents)

    parent1 = parents[i]
    parent2 = parents[pop_size - i - 1]

    return parent1, parent2


def choose_pairs(parents, i):
    """
    Choose 2 parents from the whole generation of parents.
    This pair is then used in crossover(parent1, parent2)
    """

    parent1 = parents[i]
    parent2 = parents[i + 1]

    return parent1, parent2
