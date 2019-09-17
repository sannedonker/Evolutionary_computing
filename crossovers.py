"""
HIEP HOI

bestandje met crossoversssss alleen nog even geen zin om na te denken. GROETJES
"""
import random
import numpy as np

def crossover(parent1, parent2):
    """
    Standard crossover in which you choose a position and divide the parents
    at that position and combine them in that point
    """
    # TODO: magic numbers weg --> deze nummers onderbouwen
    probality = random.uniform(0.6, 0.9)
    cut = probality * len(parent1)
    cut = int(cut)
    child1 = np.concatenate((parent1[:cut], parent2[cut:]), axis = None)
    child2 = np.concatenate((parent2[:cut], parent1[cut:]), axis = None)

    return child1, child2
