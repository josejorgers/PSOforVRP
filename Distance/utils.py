import random

def codify(perm):
    M = max([max(r) for r in perm if r != []])
    code = [-1]*(M+1)
    c = 0
    for i in range(len(perm)):
        for j in range(len(perm[i])):
            code[perm[i][j]] = c
            c+=1
    return code

def lis(source, destination):
    code = codify(source)
    try:
        counts = [[0 for _ in r] for r in destination]
    except:
        print(source)
        print(destination)
        raise Exception('No se nada!!!')

    idx = [[-1 for _ in r] for r in destination]
    dic = make_set(source)
    seek = False
    for i in range(0, len(destination)):
        for j in range(0, len(destination[i])):
            if i !=dic[destination[i][j]][0]:
                continue
            seek = True
            start = code[destination[i][j]]
            counts[i][j] = max(1,counts[i][j])
            count = counts[i][j] + 1
            for k in range(i, len(destination)):
                for l in range(0, len(destination[k])):
                    if (i==k and l <= j) or dic[destination[k][l]][0] != k:
                        continue
                    if start < code[destination[k][l]] and counts[k][l] < count:
                        counts[k][l] = count
                        idx[k][l] = (i,j)
    return [] if not seek else get_subsequence(destination, idx, max_index(counts))

def max_index(counts):
    index = 0
    M = -1
    for i in range(len(counts)):
        for j in range(len(counts[i])):
            if counts[i][j] > M:
                index = (i,j)
                M = counts[i][j]
    return index

def get_subsequence(perm, idx, index):

    if idx[index[0]][index[1]] == -1:
        return [perm[index[0]][index[1]]]
    l = get_subsequence(perm, idx, idx[index[0]][index[1]])
    l.append(perm[index[0]][index[1]])
    return l

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

if __name__ == '__main__':
    p = [1,4,3,2,5,6]
    code = [0,1,2,3,4,5,6]
    print(lis(p,code))