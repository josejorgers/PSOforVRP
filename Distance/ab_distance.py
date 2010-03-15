from Distance import utils


def step(src, tmp, to_i, to_j):

    ii, jj = -1, -1

    done = False
    for i in range(len(src)):
        for j in range(len(src[i])):
            if src[i][j] == tmp:
                ii,jj = i,j
                done = True
                break
        if done:
            break

    src[ii] = src[ii][:jj] + src[ii][jj+1:]
    while len(src) <= to_i:
        src.append([])
    j = to_j
    if ii == to_i and to_j > jj:
        j-=1
    src[to_i] = src[to_i][:j] + [tmp] + src[to_i][j:]
    return ii==to_i and to_j > jj


def distance(source, destination):

    lis = utils.lis(source, destination)
    path = [source]
    nxt = [[c for c in r] for r in source]
    for i in range(len(destination)):
        idx = 0
        for j in range(len(destination[i])):
            idx = max(idx, j)
            tmp = destination[i][j]
            if not tmp in lis:
                inv = step(nxt, tmp, i, idx)
                path.append([[c for c in r if c != -1] for r in nxt if r != []])
                if not inv:
                    idx+=1
            elif idx >= len(nxt[i]):
                continue
            else:
                while nxt[i][idx] != tmp:
                    idx+=1
                idx += 1
    return utils.clean_path(path)
