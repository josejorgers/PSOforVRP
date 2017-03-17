from Distance import utils


def preprocess(source, destination):
    src = utils.parse_solutions(source, destination)
    dest = utils.make_set(destination)
    init = utils.make_set(source)
    s,d = [],[]
    push, pop = [[] for _ in range(max(len(source), len(destination)))], \
                [[] for _ in range(max(len(source), len(destination)))]


    #Route changes
    for i in range(len(src)):
        for j in range(len(src[i])):
            if i != src[i][j][0]:
                s.append((i,j))
                d.append(src[i][j])
                push[src[i][j][0]].append(src[i][j][1])
                pop[i].append(j)

    utils.sort(s,d)
    for i in range(max(len(source), len(destination))):
        push[i] = sorted(push[i])
        pop[i] = sorted(pop[i])

    #Inversions :-(
    M = max(max(r) for r in source if r != [])
    mark = [[] for _ in range(M + 1)]
    go, stay = [], []
    for i in range(len(src)):
        for j in range(len(src[i])):
            if i != src[i][j][0]:
                continue
            ii = j #where the client must be located
            idx = src[i][j][1] #where the client must go
            b = False
            a = False
            for p in push[i]:
                if (p <= ii and ii > j) or p < ii:
                    ii+=1
                if p == j:
                    b = True
            for p in pop[i]:
                if p <= ii:
                    ii-=1
                    a = True
            if not a and b and ii==j: #just a push and it was exactly in your position
                ii+=1

            if ii > idx: #if you go to a smaller position then you will be moved
                go.append(source[i][j])
            elif ii < idx: # else, if you go to a position different to your current one
                counter = 0
                for k in range(j + 1, len(src[i])):
                    if src[i][k][0] != i:
                        continue
                    if src[i][k][1] < idx: # then let's mark the clients which have a smaller destination
                        mark[source[i][k]].append(source[i][j])#... than you
                        counter += 1
                if ii + counter - len(mark[source[i][j]]) < idx: #if moving those clients doesn't allow
                    go.append(source[i][j])#...you to get your destination, you must be moved
                else:
                    stay.append(source[i][j])#in other case maybe you don't have to be moved
            else: #if you are in your destination position
                for m in mark[source[i][j]]:
                    go.append(m)
                for k in range(j+1, len(src[i])):
                    mark[source[i][k]] = []

    used = [False]*(M+1)
    for g in go:
        if not used[g]:
            s.append(init[g])
            d.append(dest[g])
            used[g] = True

    utils.go_vs_stay(go, stay, used, mark, s, d, init, dest)

    s.reverse()
    d.reverse()
    return s,d

def step(S, src, s, d, modif, dict, counter):

    ss = s.pop()
    idx = ss[1]
    dd = d.pop()
    ii = dd[1]

    for m in modif[ss[0]]:
        if m[0] <= idx:
            idx += m[1]
    # for m in modif[dd[0]]:
    #     if m[0] < ii:
    #         ii += 1

    if ss[0] == dd[0] and idx == ii:
        if len(s) > 0:
            return counter+1, [ss] + s[0:],[dd] + d[0:]
        return None, s, d

    while len(src) <= dd[0]:
        src.append([])

    if len(src[ss[0]]) == 0:
        return None, s, d

    modif[ss[0]].append((idx, -1))
    modif[dd[0]].append((ii, 1))

    tmp = src[ss[0]][idx]
    src[ss[0]] = src[ss[0]][:idx] if idx==len(src[ss[0]])-1 else src[ss[0]][:idx]+src[ss[0]][idx+1:]
    lim = min(len(src[dd[0]]), ii)
    src[dd[0]] = src[dd[0]][:lim]+[tmp]+src[dd[0]][lim:]

    return src, None, None

def distance(source, destination):

    s,d = preprocess(source, destination)
    dict = utils.make_set(destination)
    modif = [[]for _ in range(max(len(source),len(destination)))]
    first = [[c for c in r] for r in source]
    path = [source]
    counter = 0
    while path[-1] != destination and len(s) > 0:
        nxt, ss, dd = step(source, first, s, d, modif, dict, counter)
        if not nxt:
            s, d = ss, dd
            continue
        if type(nxt)==int:
            s, d = ss, dd
            if nxt >= len(s):
                break
            counter = nxt
            continue
        first = [[c for c in r] for r in nxt]
        path.append([[c for c in r] for r in nxt if r != []])
    src = path[-1]
    p1 = [src]
    s,d = preprocess(src, destination)
    first = [[c for c in r] for r in src]
    modif = [[] for _ in range(max(len(src), len(destination)))]
    counter = 0
    while p1[-1] != destination and len(s) > 0:
        nxt, ss, dd = step(source, first, s, d, modif, dict, counter)
        if not nxt:
            s, d = ss, dd
            continue
        if type(nxt) == int:
            s, d = ss, dd
            if nxt >= len(s):
                break
            counter = nxt
            continue
        first = [[c for c in r] for r in nxt]
        p1.append([[c for c in r] for r in nxt if r != []])
    path += p1
    src = path[-1]
    p1 = [src]
    s, d = preprocess(src, destination)
    first = [[c for c in r] for r in src]
    modif = [[] for _ in range(max(len(src), len(destination)))]
    counter = 0
    while p1[-1] != destination and len(s) > 0:
        nxt, ss, dd = step(source, first, s, d, modif, dict, counter)
        if not nxt:
            s, d = ss, dd
            continue
        if type(nxt) == int:
            s, d = ss, dd
            if nxt >= len(s):
                break
            counter = nxt
            continue
        first = [[c for c in r] for r in nxt]
        p1.append([[c for c in r] for r in nxt if r != []])
    path += p1
    return utils.clean_path(path)

