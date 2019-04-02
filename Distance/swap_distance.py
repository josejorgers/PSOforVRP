from Distance import utils


def equal_len(source, destination):

    for i in range(len(source)):
        if len(source[i]) != len(destination[i]):
            return False
    return True

def preprocess(source, destination):

    INF = max([max(r) for r in source if r != []])+1

    if len(source) != len(destination):
        return None
    if not equal_len(source, destination):
        return None


    src = utils.parse_solutions(source, destination)

    curr_pos = [-1 for _ in range(INF)]
    go = [-1 for _ in range(INF)]

    for i in range(len(src)):
        for j in range(len(src[i])):
            if (i,j) != src[i][j]:
                go[source[i][j]] = src[i][j]
            curr_pos[source[i][j]] = (i,j)

    return go, curr_pos

def step(src, go, idx, curr_pos):

    dpos = go[idx]
    spos = curr_pos[idx]
    sw = src[dpos[0]][dpos[1]]


    go[idx] = -1
    if go[sw] == spos:
        go[sw] = -1
    curr_pos[sw] = spos

    new_sol = [[c for c in r] for r in src]

    new_sol[dpos[0]] = new_sol[dpos[0]][:dpos[1]] + [idx] + new_sol[dpos[0]][dpos[1]+1:]
    new_sol[spos[0]] = new_sol[spos[0]][:spos[1]] + [sw] + new_sol[spos[0]][spos[1]+1:]

    return new_sol


def distance(source, destination):

    p = preprocess(source, destination)

    if p == None:
        return p

    go, curr_pos = p[0], p[1]

    path = [source]
    src = [[c for c in r] for r in source]

    for i in range(len(go)):
        if go[i] == -1:
            continue
        nxt = step(src, go, i, curr_pos)
        path.append(nxt)
        src = [[c for c in r] for r in nxt]
    return path