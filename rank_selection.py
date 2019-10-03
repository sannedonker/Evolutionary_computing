# Gebaseerd op boek p. 82
import numpy as np


def rank_selection(pop, pop_f, N):
    """
    Rank individuals in population according to their fitness values.
    """

    # make arrays of lists
    pop = np.asarray(pop)
    pop_f = np.asarray(pop_f)

    # sort sample
    sorting = np.asarray(pop_f).argsort()
    sorted_pop = np.asarray(pop)[sorting]
    sorted_f = np.asarray(pop_f)[sorting]
    sorted_pop = np.ndarray.tolist(sorted_pop)
    sorted_f = np.ndarray.tolist(sorted_f)

    # calculate selection probability for an individual of rank i (see book p. 82)
    mu = len(pop)
    s_value = 2
    ranked_prob = []

    # LINEAR RANKING: determine fitness score based on rank
    for i in range(mu):
        prob = (2 - s_value) / mu + (2 * i * (s_value - 1)) / (mu * (mu - 1))
        ranked_prob.append(prob)

    # make wheel according to fitness scores
    top = ranked_prob[len(ranked_prob) - 1]
    wheel = [0]*len(ranked_prob)

    for i in range(1, len(ranked_prob), 1):
        wheel[i] = float(ranked_prob[i])/top

    # return roulette_wheel(sorted_pop, ranked_prob)
    mating_pool, mating_pool_f = stoch_uni_sampling(sorted_pop, sorted_f, N, wheel)
    return mating_pool, mating_pool_f


def roulette_wheel(pop, ranked_prob):
    """
    Selects members of the mating pool, given the cumulative probability distribution a.
    """

    amount = 10
    current_member = 0

    mating_pool = []
    for n in range(amount):
        r = np.random.uniform(0, 1)
        for (i, individual) in enumerate(pop):
            if r <= ranked_prob[i]:
                mating_pool.append(individual)
                break

    return mating_pool


def stoch_uni_sampling(pop, pop_f, N, wheel):
    """
    Selects members using stochastic universal sampling.
    """

    amount = N
    current_member = 0
    i = 1
    mating_pool = [0] * amount
    mating_pool_f = [0] * amount
    r = np.random.uniform(0, 1)

    # Repeat until requested amount of individuals are chosen
    while (current_member < amount):
        if(r <= wheel[i]):
            mating_pool[current_member] = pop[i]
            mating_pool_f[current_member] = pop_f[i]
            current_member += 1
            r = (r + 1 / amount) % 1
        i += 1
        i = i % len(pop)

    return mating_pool, mating_pool_f
