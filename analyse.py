# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 10:23:23 2019

@author: Eline
"""

import matplotlib.pyplot as plt

def plot(generations, f_max):
    
    #TODO: nog mean fitness adden en legend?
    plt.plot(list(range(0, generations + 1)), f_max, label = 'best')
    plt.xlabel(xlabel = 'generation number')
    plt.ylabel(ylabel = 'fitness')
    plt.title(label = 'fitness over generatations')