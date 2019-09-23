import numpy as np
import random

def choose_parents_kway(pop, pop_f, n, k):
    """
    Choose which individuals become parents with a K-way tournament
    Input: population, number of contestents: K
    Output: list of parents
    """
    parents = []
    for i in range(n):

        # choose K individuals that will enter the tournament
        tournament = []
        contestents = []


        for j in range(k):

            # make sure every individual can only compete once per tournament
            contestent = random.randint(0, n - 1 - j)

            while contestent in contestents:
                contestent = random.randint(0, n - 1 - j)
            contestents.append(contestent)

        for j in contestents:
            tournament.append(pop_f[j])

        # choose winner, add winner to the parents
        winner = tournament.index(max(tournament))
        parents.append(pop[winner])

    return parents


def choose_survivors(pop, pop_f):
    """"
    First kill the worst quarter of the generation.
    Then kill a random quarter of the generation.
    """

    # sort pop_f and then sort pop similarly
    # evt TODO: nu mega omslachtig maar alles lukte even neit en dat was kut
    sorting = np.asarray(pop_f).argsort()
    sorted_pop = np.asarray(pop)[sorting]
    sorted_f = np.asarray(pop_f)[sorting]
    sorted_pop = np.ndarray.tolist(sorted_pop)
    sorted_f = np.ndarray.tolist(sorted_f)

    # kill worst quarter
    quarter = int(len(pop) / 4)
    survivors = sorted_pop[quarter:]

    # kill a random quarter
    # TODO: de error weghalen oeepsieeee
    for i in range(quarter):
        kill = random.randint(0, len(pop) - quarter - i)
        survivors.remove(survivors[kill])

    # if less than half of the population is killed, kill more individuals
    while len(pop) / 2 != len(survivors):
        kill = random.randint(0, len(survivors))
        survivors.remove(survivors[kill])

    return(survivors)



def choose_pairs(parents, i):
    """
    Choose 2 parents from the whole generation of parents.
    This pair is then used in crossover(parent1, parent2)
    TODO: REBECCA AFMAKEN
    """

    parent1 = parents[i]
    # if i == offspring_size - 1:
    #     i = 0
    parent2 = parents[i + 1]

    return parent1, parent2
