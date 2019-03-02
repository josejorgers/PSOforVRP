from Distance import utils


def preprocess(source, destination):
    src = utils.parse_solutions(source, destination)
    s,d = [],[]

    for i in range(len(src)):
        for j in range(len(src[i])):
            if i != src[i][j][0]:
                s.append((i,j))
                d.append(src[i][j])

    for i in range(len(src)):
        for j in range(len(src[i])-1):
            for k in range(j+1,len(src[i])):
                if i == src[i][j][0] and i == src[i][k][0] and src[i][j][1] > src[i][k][1]:
                    s.append((i,j))
                    d.append(src[i][j])
                    break
    for i in range(len(s)-1):
        for j in range(i+1, len(s)):
            if s[i][1] < d[j][1] or (d[i][1] < d[j][1] and s[i][1] < s[j][1]):
                s[i], s[j] = s[j], s[i]
                d[i], d[j] = d[j], d[i]
    return s,d

def step(S, src, s, d, push, pop):

    ss = s.pop()
    idx = ss[1]
    for i in push[ss[0]]:
        if i <= ss[1]:
            idx += 1
    for i in pop[ss[0]]:
        if i <= ss[1]:
            idx -= 1
    dd = d.pop()

    while len(src) <= dd[0]:
        src.append([])
    push[dd[0]].append(dd[1])
    pop[ss[0]].append(ss[1])

    tmp = src[ss[0]][idx]
    src[ss[0]] = src[ss[0]][:idx] if idx==len(src[ss[0]])-1 else src[ss[0]][:idx]+src[ss[0]][idx+1:]
    lim = min(len(src[dd[0]]), dd[1])
    src[dd[0]] = src[dd[0]][:lim]+[tmp]+src[dd[0]][lim:]

    return src

def distance(source, destination):

    s,d = preprocess(source, destination)
    push = [[]for _ in range(max(len(source),len(destination)))]
    pop = [[]for _ in range(max(len(source),len(destination)))]
    first = [[c for c in r] for r in source]
    path = [source]
    while len(s) > 0:
        nxt = step(source, first, s, d, push, pop)
        first = [[c for c in r] for r in nxt]
        path.append([[c for c in r] for r in nxt if r != []])
    return path

