# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 10:23:23 2019

@author: Eline
"""

import matplotlib.pyplot as plt

def plot(generations, f_max, f_mean):
    """
    Function to plot results.
    """
    plt.plot(list(range(0, generations + 1)), f_max, label = 'best')
    plt.plot(list(range(0, generations + 1)), f_mean, label = 'mean')
    plt.xlabel(xlabel = 'generation number')
    plt.ylabel(ylabel = 'fitness')
    plt.title(label = 'fitness over generatations')
    plt.legend()
    plt.savefig("experiment.pdf", dpi=150)
    plt.show()
