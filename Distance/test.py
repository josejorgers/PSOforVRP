from Distance import utils,distances
from pso import random_sol

# src =[[3, 4, 7, 9], [2], [8, 6, 5], [1], [10]]
# dest =[[7, 5, 4, 2, 6, 1, 10, 8, 3, 9]]

d = 0
for _ in range(100):
    src = random_sol(5)
    dest = random_sol(5)
    # print(src)
    # print(dest)
    p1 = distances.distance(src, dest, 'rarb')
    if p1[-1] != dest:
        print('Dummy is wrong!!!')
        print(src)
        print(dest)
        print(p1[-1])
        print(utils.lis(src,dest))
        print('-------------------')
        break
# crit = 'raabrarbb'
#
# # #################################
####Testing the split_criteria###
#################################

# crs = utils.split_criteria(crit)
# for cr in crs:
#     print(cr.get_departures)
#     print(cr.get_inversions)
#     print(cr.get_insertions)
#     print('------------------')

##############################
###Testing solution parsing###
##############################

# sol = utils.parse_solutions(src,dest)
# routes = utils.parse_routes(sol)
# for r in routes:
#     print(r.get_departures)
#     print(r.get_inversions)
#     print(r.get_insertions)
#     print('------------------')

##########################
###Testing the distance###
##########################


# p = distances.distance(src, dest, 'rarb')
# print(src)
# print(dest)
# print(p[-1])