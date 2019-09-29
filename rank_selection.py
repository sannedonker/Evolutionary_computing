# Gebaseerd op boek p. 82
import numpy as np

def rank_selection(pop, pop_f, N):
    """
    Rank individuals in population according to their fitness values.
    Returns
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

    # LINEAR RANKING - WORKS
    for i in range(mu):
        prob = (2 - s_value) / mu + (2 * i * (s_value - 1)) / (mu * (mu - 1))
        ranked_prob.append(prob)

    # EXPONENTIAL RANKING - DOES NOT WORK: what is c?
    # for i in range(mu):
    #     prob = (1 - math.exp(-i)) / mu
    #     ranked_prob.append(prob)

    print("sorted pop1 {}".format(sorted_pop))
    print("sorted f1 {}".format(sorted_f))
    print("ranked_prob1: {}".format(ranked_prob))

    # make wheel according to fitness scores
    # summ = float(sum(ranked_prob))
    top = ranked_prob[len(ranked_prob)-1]
    print(top)
    # print("sum {}".format(summ))
    wheel = [0]*len(ranked_prob)
    # wheel[0] = float(ranked_prob[0])/top
    for i in range(1, len(ranked_prob), 1):
        wheel[i] = float(ranked_prob[i])/top
        # sorted_f[i] = sorted_f[i]
        # print(sorted_f[i])
        # sorted_f[i] += sorted_f[i-1]/summ
    print("sorted pop {}".format(sorted_pop))
    print("sorted f {}".format(sorted_f))
    print("sorted wheel {}".format(wheel))
    # return roulette_wheel(sorted_pop, ranked_prob)
    mating_pool, mating_pool_f = stoch_uni_sampling(sorted_pop, sorted_f, N, wheel)
    return mating_pool, mating_pool_f

    # NOG VERDER MEE WERKEN
    # total_fit = float(sum(fitness))
    # relative_fitness = [f/total_fit for f in fitness]
    # probabilities = [sum(relative_fitness[:i+1])
    #                  for i in range(len(relative_fitness))]
    # return probabilities

def roulette_wheel(pop, ranked_prob):
    """
    Selects lambda members of the mating pool, given the cumulative probability distribution a.
    """
    amount = 10
    current_member = 0

    # ZIE BOEK
    # while (current_member < amount):
    #     r = np.random.uniform(0, 1) # random getal tussen 0 en sum(ranked_prob) (=>1)
    #     i = 0
    #     while (ranked_prob[i] < r):
    #         i += 1
    #     mating_pool[current_member] = pop[i]
    #     current_member += 1
    # print(mating_pool)


    # WERKT MAAR OUTPUT ZELFDE OUDERS + NIET ALTIJD OUTPUT
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
    Selects lambda members of the mating pool, given the cumulative probability distribution a.
    """
    print("LEN uni pop {}".format(len(pop)))

    print("uni f {}".format(pop_f))
    # make arrays of lists
    # pop = np.asarray(pop)
    # pop_f = np.asarray(pop_f)
    #
    # # sort sample
    # sorting = np.asarray(pop_f).argsort()
    # # sorted_pop = (np.asarray(pop)[sorting]).tolist()
    # # sorted_f = (np.asarray(pop_f)[sorting]).tolist()
    # sorted_pop = np.asarray(pop)[sorting]
    # sorted_f = np.asarray(pop_f)[sorting]
    # sorted_pop = np.ndarray.tolist(sorted_pop)
    # sorted_f = np.ndarray.tolist(sorted_f)
    # print(sorted_f)

    # # make wheel according to fitness scores
    # summ = float(sum(sorted_f))
    # print("sum {}".format(summ))
    # wheel = [0]*len(sorted_f)
    # wheel[0] = float(sorted_f[0])/summ
    # for i in range(1, len(sorted_f), 1):
    #     wheel[i] = float(sorted_f[i])/summ + wheel[i-1]
    #     # sorted_f[i] = sorted_f[i]
    #     # print(sorted_f[i])
    #     # sorted_f[i] += sorted_f[i-1]/summ
    # print("sorted {}".format(wheel))

    amount = N
    current_member = 0
    i = 1
    mating_pool = [0] * amount
    mating_pool_f = [0] * amount
    r = np.random.uniform(0, 1)

    while (current_member < amount):
        print('loop')
        print('i: {}'.format(i))
        # print(i)
        print('r: {}'.format(r))
        # print(r)
        # i = i % len(pop)



        if(r <= wheel[i]):
            print('ranked_prob: {}'.format(wheel[i]))
            print('{} CHOSEN'.format(i))
            print('popI,popF: {},{}'.format(pop[i],pop_f[i]))
            mating_pool[current_member] = pop[i]
            mating_pool_f[current_member] = pop_f[i]
            current_member += 1
            print("current_member {}".format(current_member))
            print('r before: {}'.format(r))
            r = (r + 1 / amount) % 1
            print('r after {}'.format(r))
            print('---------1-')
        i += 1
        i = i % len(pop)


        print('----')


    # for (sum = i = 0; i < len(mating_pool); i++):
    #     for (sum += ):
    #         mating_pool[i] = pop[i]
    # print(mating_pool)


    # # WERKT (niet meer) MAAR OUTPUT ZELFDE OUDERS
    # mating_pool = []
    # for n in range(amount):
    #     r = np.random.uniform(0, 1/amount)
    #     print(r)
    #     # r= random.random()
    #     for (i, individual) in enumerate(pop):
    #         if r <= ranked_prob[i]:
    #             print("yee")
    #             mating_pool.append(individual)
    #             break
    #
    return mating_pool, mating_pool_f

# # TESTEN
# pop = [1,2,3,4,5]
# pop_f = [1,1,1,1,1]
#
# print(rank_selection(pop,pop_f))
# print("chosen: {},{}".format(chosen, chosenF))
