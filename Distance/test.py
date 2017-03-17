from Distance import utils,distances
from pso import random_sol
src = [[2, 6, 7], [3, 5], [4], [9, 8], [1, 10]]
dest = [[2], [4, 7, 9], [5, 10], [6, 8, 3], [1]]
# tests = 100
# c = 0
# e = 0
# for _ in range(1000):
#     while tests > 0:
#         src = random_sol(10)
#         dest = random_sol(10)
#         # print(src)
#         # print(dest)
#         p = distances.distance(src,dest,'rarb')
#         if p[-1] != dest:
#             print('An error has happened!!!')
#             print(src)
#             print(dest)
#             print(p[-1])
#             print('------------------------------')
#             c += 1
#         tests -= 1
#     print(c)
#     e+=c
#     c=0
#     tests = 100
# print(e/1000)
#crit = 'raabrarbb'

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

s = []
d = []
for r in src:
    for c in r:
      s.append(c)
for r in dest:
    for c in r:
      d.append(c)
s, d = [s], [d]

p = distances.distance(s, d, 'rarb')
p = p[-1][0]
# solve = []
# start = 0
# for r in dest:
#     solve.append(p[start:start+len(r)])
#     start+=len(r)


print(src)
print(dest)
print(p)