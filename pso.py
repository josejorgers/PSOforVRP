import random, protocols
from Distance import distances, utils

choices = ['rarb','rarac','rdre']

class Particle:

    def __init__(self, solution, criteria, vrange=10):
        self.solution = [[c for c in r] for r in solution]
        self.criteria = criteria
        self.own_best = [[c for c in r] for r in solution]
        self.vrange = vrange
        self.v = random.randint(1,vrange)

    def edit_solution(self,sol):

        if protocols.objective_function(sol) < protocols.objective_function(self.own_best):
            self.own_best = [[c for c in r] for r in sol]
        return [[c for c in r] for r in sol]

    def move(self, swarm_best):

        to_opt = distances.distance(self.solution, swarm_best, self.criteria)

        if not to_opt:
            target = self.own_best

        else:
            d_pbest = len(distances.distance(self.solution, self.own_best, self.criteria))
            d_tbest = len(to_opt)

            ratio = d_tbest/(d_pbest + d_tbest)
            path1 = distances.distance(self.own_best, swarm_best, self.criteria)
            idx = int(ratio*len(path1))
            target = path1[idx]

        path = distances.distance(self.solution,target, self.criteria)

        new_sol = path[min(self.v, len(path)-1)]

        if self.v > len(target):
            n = self.v-len(target)
            for i in range(n):
                tmp = [[c for c in r] for r in new_sol]
                new_sol = utils.apply(tmp, self.criteria)

        self.v = random.randint(1,self.vrange)
        self.solution = self.edit_solution(new_sol)

        return self.solution


def take_slice(l, first, end):
    r = random.randint(first+1, len(l)-end)
    return l[first:r]

def random_sol(clients):
    routes = random.randint(1,clients)
    l = [i for i in range(1,clients+1)]
    random.shuffle(l)
    sol = [[] for _ in range(routes)]

    clients_placed = 0
    for c in range(routes):
        sol[c].append(l[c])
        clients_placed += 1
    for c in range(clients_placed, len(l)):
        r = random.randint(0,routes-1)
        sol[r].append(l[c])
    return sol


def init(clients, N):
    particles = []
    for s in range(N):
        particles.append(Particle(random_sol(clients), random.choice(choices)))
    return particles


def pso(clients, N=100, iterations = 100):
    part = init(clients, N)
    opt=None
    for ss in part:
        s = ss.solution
        if not opt or protocols.objective_function(s) < protocols.objective_function(opt):
            opt = [[c for c in r] for r in s]
    it = iterations

    print(protocols.objective_function(opt))

    while it > 0:
        for p in part:
            s = p.move(opt)
            if protocols.objective_function(s) < protocols.objective_function(opt):
                opt = [[c for c in r]for r in s]
        it-=1
    solve = [[c for c in r] for r in opt if r != []]

    return solve