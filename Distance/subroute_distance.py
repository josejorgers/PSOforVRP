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

def step(S, src, s, d, push, pop):

    ss = s.pop()

    begin, end = ss[1], ss[2]

    for i in push[ss[0]]:
        begin += max(0,min(i[1], ss[1]) - i[0] + 1)
        end += max(0,min(i[1],ss[2]) - i[0] + 1)

    for i in pop[ss[0]]:
        begin -= max(0, min(i[1], ss[1]) - i[0] + 1)
        end -= max(0, min(i[1], ss[2]) - i[0] + 1)

    dd = d.pop()

    if dd[0] == ss[0] and begin == dd[1] and end == dd[2]:
        return None

    while len(src) <= dd[0]:
        src.append([])

    if ss[0] == dd[0] and begin < dd[1]:
        push[dd[0]].append((dd[1]+1, dd[2]+1))
    else:
        push[dd[0]].append((dd[1], dd[2]))

    pop[ss[0]].append((ss[1], ss[2]))

    tmp = src[ss[0]][begin:end+1]
    src[ss[0]] = src[ss[0]][:begin] + src[ss[0]][end+1:]
    src[dd[0]] = src[dd[0]][:dd[1]] + tmp + src[dd[0]][dd[1]:]

    return src

def distance(source, destination):

    s,d = preprocess(source, destination)
    push = [[]for _ in range(max(len(source),len(destination)))]
    pop = [[]for _ in range(max(len(source),len(destination)))]
    first = [[c for c in r] for r in source]
    path = [source]
    while len(s) > 0:
        nxt = step(source, first, s, d, push, pop)
        if not nxt:
            continue
        first = [[c for c in r] for r in nxt]
        path.append([[c for c in r] for r in nxt if r != []])
    return utils.clean_path(path)
