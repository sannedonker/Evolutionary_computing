#######################################################################################
# EvoMan FrameWork - V1.0 2016                                                         #
# DEMO : perceptron neural network controller evolved by Genetic Algorithm.              #
#        general solution for enemies (games)                                         #
# Author: Karine Miras                                                                    #
# karine.smiras@gmail.com                                                                 #
#######################################################################################

# imports framework
import sys,os
sys.path.insert(0, 'evoman')
from environmentclass import Environment
from demo_controller import player_controller

# imports other libs
import numpy as np

experiment_name = 'controller_generalist_demo'
if not os.path.exists(experiment_name):
    os.makedirs(experiment_name)

# initializes environment for multi objetive mode (generalist)  with static enemy and ai player
env = Environment(experiment_name=experiment_name,
                  player_controller=player_controller(),
                    speed="normal",
                  enemymode="static",
                  level=2)

# sol = np.loadtxt('solutions_demo/demo_all.txt')
sol = np.loadtxt('42.txt')
print('\n LOADING SAVED GENERALIST SOLUTION FOR ALL ENEMIES \n')

means = []
fitnesses = []
player_lifes = []
enemy_lifes = []

print(len(sol))
# tests saved demo solutions for each enemy
for en in range(1, 9):

    # Update the number of neurons for this specific example
    # env.player_controller.n_hidden = [0]
    gains_list = []
    temp1 = []
    temp2 = []
    temp3 = []

    # Repeat 5 times for this enem
    for h in range(5):

        #Update the enemy
        env.update_parameter('enemies',[en])

        f,pl,el,t = env.play(sol)

        # pl = evaluation[1]
        # el = evaluation[2]

        gains_list.append(pl - el)
        temp1.append(f)
        temp2.append(pl)
        temp3.append(el)

    means.append(np.mean(gains_list))
    fitnesses.append(np.mean(temp1))
    player_lifes.append(np.mean(temp2))
    enemy_lifes.append(np.mean(temp3))


print(means)
print(fitnesses)
print(player_lifes)
print(enemy_lifes)


#
# def test_for_all_list(solution):
#     """
#     Test the best solution for all enemies
#     """
#
#     means = []
#
#     for i in range(8):
#
#         print(i, "ENEMY NR")
#         env = Environment(experiment_name = experiment_name,
#                               enemies = [i + 1],
#                               player_controller = player_controller(),
#                               multiplemode = "no")
#
#         # Repeat 5 times for this enemy
#         for h in range(5):
#
#             gains_list = []
#
#             evaluation = evaluate_best(env, solution)
#
#             pl = evaluation[1]
#             el = evaluation[2]
#
#             gains_list.append(pl - el)
#             print(gains_list)
#
#         means.append(np.mean(gains_list))
#         print(means, "MEANS")
#
#     print(means, "GAINS")
#     return means
#
#
# best = []
#
# dinges = open("42.txt", "r")
# for line in dinges:
#
#     best.append(line.strip())
#
# print(len(best))
# print(test_for_all_list(best))
