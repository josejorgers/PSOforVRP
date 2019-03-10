import pso, protocols

import random
if __name__ == '__main__':

    clients = 60#int(input('Number of clients: ' ))
    demands = [0]

    for c in range(clients):
        d = random.randint(1,10)#int(input('Demand of client %d: ' % (c+1)))
        demands.append(d)

    matrix = [[0 for _ in range(clients+1)] for _ in range(clients+1)]

    print('Now insert the transportation costs:')
    for i in range(clients+1):
        for j in range(i+1, clients+1):
            if i==j:
                continue
            matrix[j][i] = matrix[i][j] = random.randint(1,10)#int(input('From %d to %d: ' % (i,j)))

    protocols.matrix = matrix
    protocols.demands = demands
    protocols.capacity = 1000000#int(input('Capacity of the vehicles: '))

    s = pso.pso(clients)
    for r in s:
        print(r)
    print(protocols.objective_function(s))

