from Distance import definitions
import queue

def split_criteria(criteria):

    chunks = criteria.split('r')[1:]

    result = []

    hanging = 0

    for c in chunks:
        inv, dep, ins = 0,0,0

        for i in c:
            if i == 'a':
                dep += 1

            elif hanging > 0:
                hanging-=1
                ins += 1
            else:
                inv += 1
                dep -= 1

            if dep < 0: #Not a valid criteria
                return None
        hanging += dep
        result.append(definitions.Route(inv, dep, ins))

    return result

def make_set(destination):

    s = {}

    for i in range(len(destination)):
        for j in range(len(destination[i])):
            s[destination[i][j]] = (i,j)

    return s

def parse_solutions(source, destination):

    src = []
    s = make_set(destination)

    for i in range(len(source)):
        src.append([0]*len(source[i]))
        for j in range(len(source[i])):
            src[i][j] = s[source[i][j]]

    if len(source) < len(destination):
        for i in range(len(source), len(destination)):
            src.append([])

    return src

def build_new_sol(src, changes):

    M = max(map(max, src))
    new = [[-1 for _ in range(M)]for _ in range(M)]
    used = [[False for _ in range(M)]for _ in range(M)]

    for k in changes:
        new[k[1][0]][k[1][1]] = src[k[0][0]][k[0][1]]
        used[k[0][0]][k[0][1]] = True

    for r in range(len(src)):
        for i in range(len(src[r])):
            if i < len(src[r])-1 and used[r][i]:
                src[r][i] = src[r][i+1]
                #Must be changed when including more complex criteria
                #since could be more than one used client in consecutive positions
                used[r][i] = False
                used[r][i+1] = True

    for i in range(len(src)):
        idx = 0
        for j in range(len(src[i])):
            if used[i][j]:
                continue
            while new[i][idx] != -1:
                idx+=1
            new[i][idx] = src[i][j]
            idx+=1

    return new

def count_inserts(sol):
    '''
    Counts how many insertions must be done for every route.
    :param sol:
    :return:
    '''

    routes = [0]*len(sol)

    for i in range(len(sol)):
        for t in sol[i]:
            if t[0] != i:
                routes[t[0]] += 1
    return routes

def count_inverts(sol, i):
    '''
    Counts hay many inversions must be done for every route.
    :param sol:
    :return:
    '''
    routes = 0
    dict = {}
    q = queue.Queue()

    for j in range(len(sol[i])-1):
        for k in range(j+1,len(sol[i])):
            if sol[i][k] == (i,j):
                routes += 1
                dict[sol[i][j]] = (i,j)
                q.put_nowait(sol[i][j])

    return routes, q, dict


def count_departs(sol, i):
    '''
    Counts how many departures must be done for every route.
    :param sol:
    :return:
    '''

    routes = 0
    dict = {}
    q = queue.Queue()

    for t in range(len(sol[i])):
        if sol[i][t][0] != i:
            routes += 1
            dict[sol[i][t]] = (i,t)
            q.put_nowait(sol[i][t])

    return routes, q, dict

def parse_routes(sol):


    ins = count_inserts(sol)

    routes = []

    for i in range(len(sol)):
        dep, q1, dict1 = count_departs(sol, i)
        inv, q2, dict2 = count_inverts(sol, i)

        dict1.update(dict2)

        routes.append(definitions.ClientRoute(inv,dep,ins[i],q1,q2,dict1))

    return routes

def clean_solution(sol):
    routes = [[i for i in r if i != -1] for r in  sol]
    return [r for r in routes if len(r) > 0]

# def apply_rarb(sol):
#
#     r1 = random.randint(0,len(sol))
#     r2 = random.randint(0,len(sol))
#
#     idx1 = random.randint(0, len(sol[r1]))
#     idx2 = random.randint(0, len(sol[r2]))
#
#     tmp = sol[r1][idx1]
#
#     sol[r1] = sol[r1][:idx1] + sol[min(idx1,len(sol[r1])-2)+1:len(sol[r1])]
#     sol[r2] = sol[:min(idx2,len(sol[r2])-1)+1] + [tmp] + sol[min(idx2,len(sol[r2])-2)+1:len(sol[r2])]
#
#     return [[c for c in r] for r in sol]