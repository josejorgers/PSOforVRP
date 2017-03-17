import random

def sort(s, d):

    for i in range(len(s)-1):
        for j in range(i+1,len(s)):
            if d[i][1] > d[j][1]:
                s[i], s[j] = s[j], s[i]
                d[i], d[j] = d[j], d[i]

def go_vs_stay(go, stay, used, mark, s, d, init, dest):

    counted = [False]*(len(mark))
    lbl = False
    counter = 0
    for st in stay:
        for m in mark[st]:
            if used[m]:
                lbl = True
                break
            if not counted[m]:
                counter+=1
                counted[m] = True

        if lbl:
            break
    if lbl or counter <= len(stay):
        for st in stay:
            for m in mark[st]:
                if not used[m]:
                    s.append(init[m])
                    d.append(dest[m])
                    used[m] = True
    else:
        for st in stay:
            if not used[st]:
                s.append(init[st])
                d.append(dest[st])
                used[st] = True

def is_rotation(r1, r2):

    if len(r1) != len(r2):
        return None
    mod = len(r1)
    idx = -1
    for i in range(len(r1)):
        if r1[i] == r2[0]:
            idx = i
            break
    if idx == -1:
        return None
    for i in range(len(r2)):
        if r2[i] != r1[(i+idx)%mod]:
            return None
    return idx if idx <= len(r1)-idx-1 else -len(r1)


def clean_path(path):
    idx = 0
    p = [path[0]]
    for i in range(1,len(path)):
        if p[idx] != path[i]:
            p.append(path[i])
            idx+=1
    return p

def make_set(destination):

    M = max([max(r) for r in destination if r != []])
    s = [-1]*(M+1)

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

def select_route(sol):
    total = len([r for r in sol if r != []])
    u = random.randint(0,total-1)
    for i in range(len(sol)):
        if sol[i] == []:
            continue
        if  u == 0:
            return i
        u-=1


def apply(sol, crit):
    return dicc[crit](sol)

def apply_rdre(sol):

    r1 = select_route(sol)
    r2 = random.randint(0,len(sol))

    if r2 == len(sol):
        sol.append([])

    b1 = random.randint(0, len(sol[r1])-1)
    e1 = random.randint(b1, len(sol[r1])-1)

    b2 = random.randint(0, max(0,len(sol[r2])-1))

    tmp = sol[r1][b1:e1+1]

    sol[r1] = sol[r1][:b1] + sol[r1][e1+1:]
    sol[r2] = sol[r2][:b2] + tmp + sol[r2][b2:]

    return sol

def apply_rarac(sol):

    r1 = random.randint(0, len(sol) - 1)
    r2 = random.randint(0, len(sol) - 1)
    idx1 = random.randint(0, len(sol[r1]) - 1)
    idx2 = random.randint(0, len(sol[r2]) - 1)
    tmp = sol[r1][idx1]
    sol[r1][idx1] = sol[r2][idx2]
    sol[r2][idx2] = tmp

    return sol

def apply_rarb(sol):


    r1 = select_route(sol)

    r2 = random.randint(0,len(sol))

    if r2 == len(sol):
        sol.append([])

    idx1 = random.randint(0, len(sol[r1])-1)
    idx2 = random.randint(0, len(sol[r2]))

    if r2 != len(sol)-1 and idx2 == len(sol[r2]):
        idx2 -= 1

    tmp = sol[r1][idx1]

    sol[r1] = sol[r1][:idx1] if idx1 == len(sol[r1]) else sol[r1][:idx1] + sol[r1][idx1+1:]
    lim = min(len(sol[r2]), idx2)
    sol[r2] = sol[r2][:lim] + [tmp] + sol[r2][lim:]

    return sol

dicc = {
    'rarb' : apply_rarb,
    'rarac' : apply_rarac,
    'rdre' : apply_rdre
}