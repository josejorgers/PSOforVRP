from Distance import ab_distance, swap_distance, subroute_distance

distances = {
    'rarb' : ab_distance.distance,
    'rarac' : swap_distance.distance,
    'rdre' : subroute_distance.distance
}

def distance(source, destination, criteria):
    return distances[criteria](source, destination)

# def ab_step(source, destination, criteria = 'rarb'):
#
#     crit = utils.split_criteria(criteria)
#     src = utils.parse_solutions(source, destination)
#
#     parsed = utils.parse_routes(src)
#
#     f = first(parsed, crit[0])
#     route = parsed[f]
#
#     changed = False
#
#     #Here we will have a while loop which will stop when the criteria application will be done
#     if route.get_inversions > 0: #For every one-step-fixable inversion in the route
#         route.make_inversion()
#         changed = True
#     elif route.get_departures > 0: #For every one-step-fixable departure in the route
#         client = route.make_departure()
#         #Maybe here we want to know where the 'b' which inserts this 'a' is
#         parsed[client[0]].make_insertion()#Then we fix the next route with its criteria_route
#         changed = True
#
#     next_sol = utils.build_new_sol(source, route.changes) #Will be the union of the changes in every route
#
#     return next_sol, changed

# def first(routes, criteria):
#     first = 0
#     M = -5
#
#     for r in range(len(routes)):
#         u = ab_usage(routes[r], criteria)
#         if u > M:
#             first = r
#             M = u
#     return first


# def ab_usage(route, criteria_chunk):
#
#     usage = 0
#
#     if route.get_departures > 0:
#         if criteria_chunk.get_departures > 0:
#             usage += 1
#         else:
#             usage -= 1
#     if route.get_inversions > 0:
#         if criteria_chunk.get_inversions > 0:
#             usage += 1
#         else:
#             usage -= 1
#     if route.get_insertions > 0:
#         if criteria_chunk.get_insertions > 0:
#             usage += 1
#         else:
#             usage -= 1
#
#     return usage

# def ab_distance(source, destination, criteria = 'rarb'):
#
#     stop = True
#     path = [source]
#     src = [[j for j in r] for r in source]
#     while stop:
#         nxt, stop = ab_step(src, destination)
#         next = utils.clean_solution(nxt)
#         path.append(next)
#         src = [[j for j in r] for r in next]
#     return path[:-1]