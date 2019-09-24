# Gebaseerd op boek p. 82 

def rank_selection(pop, pop_f):
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


    print("ranked_prob")

    print(ranked_prob)

    # return roulette_wheel(sorted_pop, ranked_prob)
    return stoch_uni_sampling(sorted_pop, ranked_prob)

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

def stoch_uni_sampling(pop, ranked_prob):
    """
    Selects lambda members of the mating pool, given the cumulative probability distribution a.
    """
    amount = 1
    current_member = i = 1

    mating_pool = [0] * amount
    r = np.random.uniform(0, 1 / amount)
    print(r)
    while (current_member < amount):
        while (r <= ranked_prob[i]):
            mating_pool[current_member] = pop[i]
            r += 1 / amount
            current_member += 1
        i += 1


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
    return mating_pool

# TESTEN
pop = [8,7,6,5,4,3,2]
pop_f = [1,2,5,9,30,60,70]

chosen = rank_selection(pop,pop_f)
print("chosen")
print(chosen)
exit(1)
