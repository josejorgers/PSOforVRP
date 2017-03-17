from Distance import utils,distances
from pso import random_sol
# src = [[2], [3], [1]]
# dest = [[2, 1, 3]]
d = 0
for _ in range(10000):
    src = random_sol(10)
    dest = random_sol(10)
    # print(src)
    # print(dest)
    p1 = distances.distance(src, dest, 'rdre')
    if p1[-1] != dest:
        print('Dummy is wrong!!!')
        print(src)
        print(dest)
        print(p1[-1])
        print('-------------------')
        break
    print(d)
#
# # crit = 'raabrarbb'

#################################
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


# p = distances.distance(src, dest, 'rdre')
# print(src)
# print(dest)
# print(p[-1])