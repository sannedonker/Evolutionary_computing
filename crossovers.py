"""
Run crossover with two parents (parent1 and parent2).
Returns two children (child1 and child2).
"""
import random
import numpy as np

def crossover(parent1, parent2, cross_min, cross_max):
    """
    Standard crossover in which you choose a position and divide the parents
    at that position and combine them in that point
    """

    probality = random.uniform(cross_min, cross_max)
    cut = probality * len(parent1)
    cut = int(cut)
    child1 = np.concatenate((parent1[:cut], parent2[cut:]), axis = None)
    child2 = np.concatenate((parent2[:cut], parent1[cut:]), axis = None)

    return child1, child2
