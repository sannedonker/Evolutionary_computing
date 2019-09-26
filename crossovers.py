"""
Run crossover with two parents (parent1 and parent2).
Returns two children (child1 and child2).
"""
import random
import numpy as np

def crossover(parent1, parent2):
    """
    Standard crossover in which you choose a position and divide the parents
    at that position and combine them in that point
    """
    # TODO: magic numbers weg --> deze nummers onderbouwen
    # print("Parent1:", parent1)
    # print("Parent2:", parent2)
    probality = random.uniform(0.5, 0.9)
    cut = probality * len(parent1)
    cut = int(cut)
    child1 = np.concatenate((parent1[:cut], parent2[cut:]), axis = None)
    child2 = np.concatenate((parent2[:cut], parent1[cut:]), axis = None)

    return child1, child2
