import random

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


def apply_rarb(sol):


    while True:
        r1 = random.randint(0,len(sol)-1)
        if len(sol[r1]) > 0:
            break

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