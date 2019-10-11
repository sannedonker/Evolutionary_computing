import numpy as np


def non_uni_mutation(pop, env, bound_min, bound_max, sigma, chance):
    """
    Non-uni mutation.
    """

    changed = 0

    for i in range(0, len(pop) - 1):
        for j in range(0, len(pop[i]) - 1):
            chance = np.random.uniform(0, 1)
            if chance <= chance:
                changed += 1
                mutation_value = np.random.uniform(-sigma, sigma)
                pop[i][j] = pop[i][j] + mutation_value

                while pop[i][j] < bound_min:
                    pop[i][j] = pop[i][j] / 2
                while pop[i][j] > bound_max:
                    pop[i][j] = pop[i][j] / 2

    pop_f, pop_pl, pop_el = evaluate(env, pop)

    return pop, pop_f

def uni_mutation(pop, env, bound_min, bound_max):
    """
    Uni-mutation.
    """
    # Replaces a value with a random generated value between the max and min bounds
    # Mutation p should be somewhere between 1 / pop_size and 1 / chromosome_length
    pop_size = len(pop)
    mutation_p = 1 / pop_size

    for i in range(0, len(pop) - 1):
        for j in range(0, len(pop[i]) - 1):
            chance = np.random.uniform(0, 1)
            if chance <= mutation_p:
                mutation_value = np.random.uniform(bound_min, bound_max)
                pop[i][j] = mutation_value

    pop_f, pop_pl, pop_el = evaluate(env, pop)

    return pop, pop_f, pop_pl, pop_el


def scramble_mutation(pop, env):
    """
    Mutate parents by scrambling up genes in a specific fragment of the chromosome.
    """

    mutation_p = 1 / len(pop)
    num_of_genes = 4
    length = len(pop[0])

    # Repeat for each individual
    for parent in pop:

        # Mutate based on mutation probability
        chance = np.random.uniform(0, 1)
        if chance <= mutation_p:

            # Switch specified amount of genes
            for i in range(num_of_genes):
                r1 = int(np.random.uniform(0, length))
                r2 = int(np.random.uniform(0, length))

                while (r1 >= r2):
                    r1 = int(np.random.uniform(0, length))
                    r2 = int(np.random.uniform(0, length))

                for i in range(num_of_genes * 2):
                    i1 = int(np.random.uniform(r1, r2 + 1))
                    i2 = int(np.random.uniform(r1, r2 + 1))

                    # Switch
                    temp = parent[i1]
                    parent[i1] = parent[i2]
                    parent[i2] = temp

    # Re-evaluate population
    pop_f, pop_pl, pop_el = evaluate(env, pop)

    return pop, pop_f, pop_pl, pop_el


def evaluate(env, pop):
    """
    Evaluate the population.
    """
    pop_f = []
    pop_pl = []
    pop_el = []

    for individual in pop:
        fitness, player_life, enemy_life, time = env.play(pcont=individual)
        pop_f.append(fitness)
        pop_pl.append(player_life)
        pop_el.append(enemy_life)

    return pop_f, pop_pl, pop_el
