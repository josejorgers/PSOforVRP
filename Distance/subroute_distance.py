from Distance import utils, ab_distance

def preprocess(source, destination):

    s,d = ab_distance.preprocess(source, destination)

    for i in range(len(s)-1):
        for j in range(i+1,len(s)):
            if s[i][0] > s[j][0] or (s[i][0] == s[j][0] and s[i][1] > s[j][1]):
                s[i], s[j] = s[j], s[i]
                d[i], d[j] = d[j], d[i]

    ss, dd = [],[]
    i = 0
    while i < len(s):
        j = i+1
        begin = s[i][1]
        dbegin = d[i][1]
        while j < len(s) and s[i][0] == s[j][0] and d[i][0]==d[j][0] and s[i][1] == s[j][1]-1 and d[i][1]==d[j][1]-1:
            i+=1
            j+=1
        ss.append((s[i][0], begin, s[i][1]))
        dd.append((d[i][0], dbegin, d[i][1]))
        i+=1

    return ss,dd

def step(S, src, s, d, modif, counter):

    ss = s.pop()
    idx, idx2 = ss[1], ss[2]
    dd = d.pop()
    ii, ii2 = dd[1], dd[2]

    for m in modif[ss[0]]:
        if m[0] <= idx:
            M = m[1] - m[0] + 1
            idx += m[2]*M
            idx2 += m[2]*M

    if ss[0] == dd[0] and idx == ii and idx2 == ii2:
        if len(s) > 0:
            return counter+1, [ss] + s[0:],[dd] + d[0:]
        return None, s, d

    while len(src) <= dd[0]:
        src.append([])

    if len(src[ss[0]]) == 0:
        return None, s, d

    modif[ss[0]].append((idx, idx2, -1))
    modif[dd[0]].append((ii, ii2, 1))

    tmp = src[ss[0]][idx:idx2+1]
    src[ss[0]] = src[ss[0]][:idx]+src[ss[0]][idx2+1:]
    lim = min(len(src[dd[0]]), ii)
    src[dd[0]] = src[dd[0]][:lim]+tmp+src[dd[0]][lim:]

    return src, None, None


def distance(source, destination):

    s,d = preprocess(source, destination)
    modif = [[]for _ in range(max(len(source),len(destination)))]
    first = [[c for c in r] for r in source]
    path = [source]
    counter = 0
    while path[-1] != destination and len(s) > 0:
        nxt, ss, dd = step(source, first, s, d, modif, counter)
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
        nxt, ss, dd = step(source, first, s, d, modif, counter)
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
        nxt, ss, dd = step(source, first, s, d, modif, counter)
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
        nxt, ss, dd = step(source, first, s, d, modif, counter)
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
