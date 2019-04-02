from Distance import utils

def step(source, destination, i, j):

    l = []
    jj = j
    a, b, c = 0, -1, 0
    for x in range(len(source)):
        for y in range(len(source[x])):
            try:
                if source[x][y] == destination[i][jj] and b == -1:
                    a, b, c = x, y, y
                    jj+=1
                    l.append(source[x][y])
                elif source[x][y] == destination[i][jj]:
                    c += 1
                    jj += 1
                    l.append(source[x][y])
                elif b != -1:
                    break
            except:
                break
        if b != -1:
            break
    source[a] = source[a][:b] + source[a][c+1:]
    while i >= len(source):
        source.append([])
    source[i] = source[i][:j] + l + source[i][j:]
    return source, jj

def distance(source, destination):

    i, j = 0, 0
    path = [[[c for c in r] for r in source]]
    first = [[c for c in r] for r in source]
    while i < len(destination):
        j = 0
        while j < len(destination[i]):
            nxt, jj = step(first, destination, i, j)
            first = [[c for c in r] for r in nxt]
            path.append([[c for c in r] for r in nxt if r != []])
            j = jj
        i+=1
    return utils.clean_path(path)
