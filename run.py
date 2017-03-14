import pso, protocols

import random, json, time
if __name__ == '__main__':

    clients = 32#int(input('Number of clients: ' ))
    demands = json.load(open('a-n33-demandas.txt'))

    # for c in range(clients):
    #     d = random.randint(1,10)#int(input('Demand of client %d: ' % (c+1)))
    #     demands.append(d)

    matrix = json.load(open('a-n33-distancia.txt'))#[[0 for _ in range(clients+1)] for _ in range(clients+1)]

    # print('Now insert the transportation costs:')
    # for i in range(clients+1):
    #     for j in range(i+1, clients+1):
    #         if i==j:
    #             continue
    #         matrix[j][i] = matrix[i][j] = max(i,j)#int(input('From %d to %d: ' % (i,j)))

    protocols.matrix = matrix
    protocols.demands = demands
    protocols.capacity = 100#int(input('Capacity of the vehicles: '))
    print(len(demands))
    print(len(matrix))

    s = pso.pso(clients)
    for r in s:
        print(r)
    print(protocols.objective_function(s))

    print(time.process_time())