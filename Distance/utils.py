from Distance import definitions

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

def get_source(source, destination):

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

def parse_solutions(source, destination):
    return get_source(source,destination)

def build_new_sol(src, changes):

    M = max(map(max, src))
    new = [[0]*M]*M

    for k in changes.keys():
        val = changes[k]
        new[val[0]][val[1]] = src[k[0]][k[1]]

    return new

def count_inserts(sol):
    '''
    Counts how many insertions must be done for every route.
    :param sol:
    :return:
    '''

    routes = [0]*len(sol)

    for r in range(len(sol)):
        for t in sol[r]:
            if t[0] != r:
                routes[t[0]] += 1
    return routes

def count_inverts(sol):
    '''
    Counts hay many inversions must be done for every route.
    :param sol:
    :return:
    '''
    routes = [0]*len(sol)

    for i in range(len(sol)):
        for j in range(len(sol[i])-1):
            for k in range(1,len(sol[i])):
                if sol[i][j][0] == i and sol[i][k][0] == i and sol[i][j][1] > sol[i][k][1]:
                    routes[i] += 1
    return routes


def count_departs(sol):
    '''
    Counts how many departures must be done for every route.
    :param sol:
    :return:
    '''

    routes = [0] * len(sol)

    for r in range(len(sol)):
        for t in sol[r]:
            if t[0] != r:
                routes[r] += 1
    return routes

def parse_routes(sol):

    dep = count_departs(sol)
    inv = count_inverts(sol)
    ins = count_inserts(sol)

    routes = []
    for i in range(len(dep)):
        routes.append(definitions.Route(inv[i],dep[i],ins[i]))

    return routes