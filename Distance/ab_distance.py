from Distance import utils

def step(source, destination, i, j):

    c = destination[i][j]
    ii, jj = 0,0
    for a in range(len(source)):
        for b in range(len(source[a])):
            if source[a][b] == c:
                ii, jj = a, b
                break
    while len(source) <= i:
        source.append([])
    source[ii] = source[ii][:jj] + source[ii][jj+1:]
    source[i] = source[i][:j] + [c] +source[i][j:]
    return source

def distance(source, destination):

    path = [source]
    first = [[c for c in r] for r in source]
    for i in range(len(destination)):
        for j in range(len(destination[i])):
            nxt = step(first, destination, i, j)
            first = [[c for c in r] for r in nxt]
            path.append([[c for c in r]for r in nxt if r != []])
    return utils.clean_path(path)