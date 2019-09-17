import numpy as np
from random import randint

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
            contestent = randint(0, n - 1 - j)
            while contestent in contestents:
                contestent = randint(0, n - 1 - j)
            contestents.append(contestent)

        for j in contestents:
            tournament.append(pop_f[j])

        # choose winner, add winner to the parents
        winner = tournament.index(max(tournament))
        parents.append(pop[winner])

    return parents

def choose_new_generation(pop, pop_f):
    """"
    sdfsdf
    """
