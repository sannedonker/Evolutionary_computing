import numpy as np
import random

CONVERGENCE = 3
KEEP_PERCENTAGE = 10
KILL_PART = 4

def sort_population(pop, pop_f):
    """
    Sort population from worst to best based on fitness
    """
    # evt TODO: nu mega omslachtig maar alles lukte even neit en dat was kut

    sorting = np.asarray(pop_f).argsort()
    sorted_pop = np.asarray(pop)[sorting]
    sorted_f = np.asarray(pop_f)[sorting]
    sorted_pop = np.ndarray.tolist(sorted_pop)
    sorted_f = np.ndarray.tolist(sorted_f)

    print(sorted_pop, sorted_f, "SORTED!!!!!!!")
    return sorted_pop, sorted_f


def choose_parents_kway(pop, pop_f, n, k):
    """
    Choose which individuals become parents with a K-way tournament
    Input: population, number of contestents: K
    Output: list of parents
    """
    parents = []
    parents_f = []
    index_list_MAGWEGOOIT = []
    for i in range(n):

        # choose K individuals that will enter the tournament
        tournament = []
        tournament_f = []
        contestents = []
        tournament_c = []

        for j in range(k):

            # make sure every individual can only compete once per tournament
            contestent = random.randint(0, n - 1)
            while contestent in contestents:
                contestent = random.randint(0, n - 1)
            contestents.append(contestent)

        # contestents is an array of random numbers between 0 and n-1
        for m in contestents:
            tournament.append(pop[m])
            tournament_f.append(pop_f[m])

            # TODO: Sannie deze regel kan toch ook weg?
            tournament_c.append(m)

        # choose winner, add winner to the parents
        winner = tournament_f.index(max(tournament_f))
        # index_contest = tournament_c[winner]
        parents.append(tournament[winner])
        parents_f.append(tournament_f[winner])
        # index_list_MAGWEGOOIT.append(index_contest)

    # TODO: print dingen weghalen en contest ook, maar wel nu nog even houden
    # om allemaal shit te chekcennefnenenr

    # print("fitness of paretns")
    # print(parents_f)
    # print(index_list_MAGWEGOOIT)

    return parents, parents_f


def choose_survivors(pop, pop_f):
    """"
    First kill the worst quarter of the generation.
    Then kill a random quarter of the generation.
    """

    # sort pop_f and then sort pop similarly
    sorted_pop, sorted_f = sort_population(pop, pop_f)

    # always keep best KEEP_PERCENTAGE percent of population
    top = int(len(pop) / KEEP_PERCENTAGE)
    must_survive = sorted_pop[(len(pop) - top):]
    must_survive_f = sorted_f[(len(pop) - top):]
    # print(must_survive_f)

    # kill worst part
    quarter = int(len(pop) / KILL_PART)
    survivors = sorted_pop[quarter:]
    survivor_fitness = sorted_f[quarter:]

    # kill a random quarter
    for i in range(quarter):
        kill = random.randint(0, len(survivors) - 1)

        # make sure the best individuals survive, when population converges kill anyway
        i = 0
        while survivors[kill] in must_survive and i < CONVERGENCE:
            kill = random.randint(0, len(survivors) - 1)
            i += 1

        survivors.remove(survivors[kill])
        survivor_fitness.remove(survivor_fitness[kill])

    # if less than half of the population is killed, kill more individuals
    while len(pop) / 2 != len(survivors):
        kill = random.randint(0, len(survivors) - 1)
        survivors.remove(survivors[kill])
        survivor_fitness.remove(survivor_fitness[kill])

    survivors = np.array(survivors)

    return(survivors, survivor_fitness)


def choose_sorted_pairs(parents, parents_f, i, pop_size):
    """
    Let the parents mate based on fitness
    Worst parent mates with best parent
    """

    parents, parents_f = sort_population(parents, parents_f)
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
