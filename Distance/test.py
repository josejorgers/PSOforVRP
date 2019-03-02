from Distance import utils,distances

dest = [[3,2],[1]]#[[i for i in range(1,201)]]
src =  [[1],[2],[3]]#[[i for i in range(200,0,-1)]]
crit = 'raabrarbb'

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
p = distances.distance(src, dest, 'rarb')
print(p)
