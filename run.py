import pso, protocols

import json, time
if __name__ == '__main__':

    clients = int(input('Number of clients: ' ))
    demands = json.load(open(input("Demand's file name: ")))

    # for c in range(clients):
    #     d = random.randint(1,10)#int(input('Demand of client %d: ' % (c+1)))
    #     demands.append(d)

    matrix = json.load(open(input("Matrix of cost's file name: ")))#[[0 for _ in range(clients+1)] for _ in range(clients+1)]

    # print('Now insert the transportation costs:')
    # for i in range(clients+1):
    #     for j in range(i+1, clients+1):
    #         if i==j:
    #             continue
    #         matrix[j][i] = matrix[i][j] = max(i,j)#int(input('From %d to %d: ' % (i,j)))

    protocols.matrix = matrix
    protocols.demands = demands
    protocols.capacity = 100#int(input('Capacity of the vehicles: '))

    N = int(input('Number of particles: '))
    it = int(input('Number of iterations: '))
    s = pso.pso(clients, N=N,iterations=it)
    for r in s:
        print(r)
    print(protocols.objective_function(s))

    print(time.process_time()/60)