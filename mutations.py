import numpy as np

# TODO: varying mutation step size?
MUTATION_SIG = 0.5

# TODO: Mutation hier ook tussen 1 / pop_size & 1 / chromosome_length?
MUTATION_P = 0.15


def non_uni_mutation(pop, env, bound_min, bound_max, sigma, chance):

    # TODO: kiezen of je eerst individuen voor mutatie wilt selecteren en daarna per gen ook nog wilt selecteren
    # of of je per gen gewoon wilt selecteren, dan kunnen er ook individuen zijn met meerdere mutaties.
    # dat laatste lijkt me beter omdat het meer random is.
    # daarna nog kijken of ik dat self-adaptive mutation ook nog wil toepassen

    changed = 0

    for i in range(0, len(pop) - 1):

        #TODO: zorg dat na mutation de value niet buiten - 1 en 1 valt
        for j in range(0, len(pop[i]) - 1):
            chance = np.random.uniform(0, 1)
            if chance <= chance:
                changed +=1
                mutation_value = np.random.uniform(-sigma, sigma)
                pop[i][j] = pop[i][j] + mutation_value

                while pop[i][j] < bound_min:
                    pop[i][j] = pop[i][j] / 2
                while pop[i][j] > bound_max:
                    pop[i][j] = pop[i][j] / 2

    pop_f = evaluate(env, pop)[0]

    return pop, pop_f

def uni_mutation(pop, env, bound_min, bound_max):

    # replaces a value with a random generated value between the max and min bounds

    # Mutation p should be somewhere between 1 / pop_size and 1 / chromosome_length
    pop_size = len(pop)
#    chromosome_length = len(pop[0])
    mutation_p = 1 / pop_size

    for i in range(0, len(pop) - 1):
        for j in range(0, len(pop[i]) - 1):
            chance = np.random.uniform(0, 1)
            if chance <= mutation_p:
                mutation_value = np.random.uniform(bound_min, bound_max)
                pop[i][j] = mutation_value

    print(pop[0])

    pop_f = evaluate(env, pop)[0]

    return pop, pop_f


def scramble_mutation(pop):
    """
    Mutate parents by scrambling up genes in a specific fragment of the chromosome.
    """
    
    # TODO: slechts deel van gen muteren: (optional) minimal and maximal mutation point kiezen
    print(pop)
    num_of_genes = 4
    length = len(pop[0])
    for parent in pop:
        for i in range(num_of_genes):
            r1 = int(random.uniform(0, length))
            r2 = int(random.uniform(0, length))
            while (r1 >= r2):
                r1 = int(random.uniform(0, length))
                r2 = int(random.uniform(0, length))
            for i in range(num_of_genes*2):
                i1 = int(random.uniform(r1, r2 + 1))
                i2 = int(random.uniform(r1, r2 + 1))
                a = parent[i1]
                parent[i1] = parent[i2]
                parent[i2] = a

    return pop


def evaluate(env, pop):
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
