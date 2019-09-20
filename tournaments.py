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


def choose_survivors(pop, pop_f, n):
    """"
    First kill the worst quarter of the generation.
    Then kill a random quarter of the generation.
    """

    # sorted_f = [x for _, x in sorted(zip(pop_f, pop))]
    test = np.asarray([3, 2, 1])
    hoi = np.asarray([4, 5, 6])

    # zipped_together = zip(pop_f, pop)
    # zipped_together.sort()
    # sorted_pop = [i for pop_f, i in zipped_together]
    # sorted_f = pop_f.sort()
    #
    # print(sorted_f)


    # print(test[test.argsort()])
    # print(hoi[test.argsort()])
    #
    sorting = np.asarray(pop_f).argsort()
    sorted_pop = np.asarray(pop)[sorting]
    sorted_f = np.asarray(pop_f)[sorting]

    sorted_pop = np.ndarray.tolist(sorted_pop)
    sorted_f = np.ndarray.tolist(sorted_f)

    print(len(pop))

    quarter = int(n / 2)
    print(int(n / 2))
    survivors = sorted_pop[quarter:]

    # print(survivors)
    # print(type(survivors))


    for i in range(quarter):
        killed = random.randint(0, n - quarter - i)
        # print(survivors[killed])
        survivors.remove(survivors[killed])

    print(len(sorted_pop))
    print(len(survivors))




def choose_pairs(parents, i, offspring_size):
    """
    Choose 2 parents from the whole generation of parents.
    This pair is then used in crossover(parent1, parent2)
    """

    parent1 = parents[i]

    if i == offspring_size - 1:
        i = 0
    parent2 = parents[i + 1]

    return parent1, parent2
