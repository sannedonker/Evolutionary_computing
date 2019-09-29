import numpy as np
import random

MUTATION_P = 0.1
MUTATION_SIG = 0.01 # The studies of Waghoo & Pervez(2013) on random mutation technique has shown that optimum probability of mutation lies between 0.0-0.3.

# population = np.loadtxt(fname = 'TESTEN/results.txt', delimiter = '  ')
population = []
print(population)


def non_uni_mutation(pop, env):

    # TODO: kiezen of je eerst individuen voor mutatie wilt selecteren en daarna per gen ook nog wilt selecteren
    # of of je per gen gewoon wilt selecteren, dan kunnen er ook individuen zijn met meerdere mutaties.
    # dat laatste lijkt me beter omdat het meer random is.
    # daarna nog kijken of ik dat self-adaptive mutation ook nog wil toepassen
    changed = 0

    for individual in pop:
        genes_to_scramble = []

        for gene in individual:
            chance = np.random.uniform(0, 1)
            if chance <= MUTATION_P:
                changed +=1
                print("GENE NOW:")
                print(gene)
                mutation_value = np.random.uniform(-MUTATION_SIG, MUTATION_SIG)
                gene = gene + mutation_value
                print("changing with value of:")
                print(mutation_value)
                print("Gene after:")
                print(gene)

        if changed > 0:
            pop_f = evaluate(env, pop)[0]
            print("OLD MEAN")
            print(np.mean(env.solutions[1]))
            print("old best")
            print(max(env.solutions[1]))
            print("NEW MEAN")
            print(np.mean(pop_f))
            print("new best")
            print(max(pop_f))

        return pop, pop_f

# inverse mutation
# cut_index = int(len(parent1) * random.uniform(0.6, 0.9))

# scramble mutation
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

pop = ([0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9])
print(scramble_mutation(pop))
