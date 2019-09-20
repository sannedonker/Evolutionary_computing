import numpy as np

MUTATION_P = 0.1
MUTATION_SIG = 0.01


def non_uni_mutation(pop, env):

    # TODO: kiezen of je eerst individuen voor mutatie wilt selecteren en daarna per gen ook nog wilt selecteren
    # of of je per gen gewoon wilt selecteren, dan kunnen er ook individuen zijn met meerdere mutaties.
    # dat laatste lijkt me beter omdat het meer random is.
    # daarna nog kijken of ik dat self-adaptive mutation ook nog wil toepassen
    changed = 0

    for individual in pop:
        
        #TODO: zorg dat na mutation de value niet buiten - 1 en 1 valt
        for gene in individual:
            chance = np.random.uniform(0, 1)
            if chance <= MUTATION_P:
                changed +=1
                mutation_value = np.random.uniform(-MUTATION_SIG, MUTATION_SIG)
                gene = gene + mutation_value

    pop_f = evaluate(env, pop)[0]

    return pop, pop_f

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
