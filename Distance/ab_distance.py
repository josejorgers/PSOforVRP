from Distance import utils


def preprocess(source, destination):
    src = utils.parse_solutions(source, destination)
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


    #Inversions
    for i in range(len(src)):
        for j in range(len(src[i])):
            if src[i][j][0] == i:
                idx = j
                for k in push[i]:
                    if k <= j:
                        idx+=1
                for k in pop[i]:
                    if k <= j:
                        idx-=1
                if idx != src[i][j][1]:
                    s.append((i,j))
                    d.append(src[i][j])
    s.reverse()
    d.reverse()
    return s,d

def step(S, src, s, d, push, pop, dict, destination):

    ss = s.pop()
    idx = ss[1]
    for i in push[ss[0]]:
        if i <= ss[1]:
            idx += 1
    for i in pop[ss[0]]:
        if i <= ss[1]:
            idx -= 1
    dd = d.pop()

    if ss[0] == dd[0] and idx == dd[1]:
        return None
    if ss[0] == dd[0]:
        r = utils.is_rotation(src[ss[0]], destination[ss[0]])
        if r == None:
            pass
        else:
            if r > 0:
                src[ss[0]] = src[ss[0]][1:]+[src[ss[0]][0]]
                s.append(ss)
                d.append(dd)
                return src
            elif r < 0:
                src[ss[0]] = [src[ss[0]][len(src[ss[0]])-1]]+src[ss[0]][:len(src[ss[0]])-1]
                s.append(ss)
                d.append(dd)
                return src
            else:
                return None

    while len(src) <= dd[0]:
        src.append([])

    ii = dd[1]
    # if dd[0] != ss[0]:
    done = False
    for i in range(dd[1], len(src[dd[0]])):
        v = dict[src[dd[0]][i]]
        if v[0] == dd[0] and v[1] < i - 1:
            ii += 1
            done = True
        else:
            break
    if not done:
        for i in range(min(dd[1],len(src[dd[0]])) - 1, -1, -1):
            v = dict[src[dd[0]][i]]
            if v[0] == dd[0] and v[1] > i + 1:
                ii-=1
            else:
                break

    if dd[0] == ss[0] and idx < dd[1]:
        push[dd[0]].append(ii+1)
    else:
        push[dd[0]].append(ii)
    pop[ss[0]].append(ss[1])

    tmp = src[ss[0]][idx]
    src[ss[0]] = src[ss[0]][:idx] if idx==len(src[ss[0]])-1 else src[ss[0]][:idx]+src[ss[0]][idx+1:]
    lim = min(len(src[dd[0]]), ii)
    src[dd[0]] = src[dd[0]][:lim]+[tmp]+src[dd[0]][lim:]

    return src

def distance(source, destination):

    s,d = preprocess(source, destination)
    dict = utils.make_set(destination)
    push = [[]for _ in range(max(len(source),len(destination)))]
    pop = [[]for _ in range(max(len(source),len(destination)))]
    first = [[c for c in r] for r in source]
    path = [source]
    while path[-1] != destination and len(s) > 0:
        nxt = step(source, first, s, d, push, pop, dict, destination)
        if not nxt:
            continue
        first = [[c for c in r] for r in nxt]
        path.append([[c for c in r] for r in nxt if r != []])
    return utils.clean_path(path)

