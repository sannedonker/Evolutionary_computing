import numpy as np

MUTATION_SIG = 0.2

# TODO: Mutation hier ook tussen 1 / pop_size & 1 / chromosome_length?
MUTATION_P = 0.1


def non_uni_mutation(pop, env, bound_min, bound_max):

    # TODO: kiezen of je eerst individuen voor mutatie wilt selecteren en daarna per gen ook nog wilt selecteren
    # of of je per gen gewoon wilt selecteren, dan kunnen er ook individuen zijn met meerdere mutaties.
    # dat laatste lijkt me beter omdat het meer random is.
    # daarna nog kijken of ik dat self-adaptive mutation ook nog wil toepassen
    
    changed = 0

    for i in range(0, len(pop) - 1):
        
        #TODO: zorg dat na mutation de value niet buiten - 1 en 1 valt
        for j in range(0, len(pop[i]) - 1):
            chance = np.random.uniform(0, 1)
            if chance <= MUTATION_P:
                changed +=1
                mutation_value = np.random.uniform(-MUTATION_SIG, MUTATION_SIG)
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
