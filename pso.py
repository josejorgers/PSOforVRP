import random, protocols
from Distance import distances, utils

class Particle:

    def __init__(self, solution, criteria = 'rarb'):
        self.solution = [[c for c in r] for r in solution]
        self.criteria = criteria
        self.own_best = [[c for c in r] for r in solution]
        self.v = random.randint(1,10)

    def edit_solution(self,sol):

        if protocols.objective_function(sol) < protocols.objective_function(self.own_best):
            self.own_best = [[c for c in r] for r in sol]
        return [[c for c in r] for r in sol]

    def move(self, swarm_best):

        d_pbest = len(distances.distance(self.solution, self.own_best, self.criteria))
        d_tbest = len(distances.distance(self.solution, swarm_best, self.criteria))

        ratio = d_tbest/(d_pbest + d_tbest)
        path1 = distances.distance(self.own_best, swarm_best, self.criteria)
        idx = int(ratio*len(path1))
        target = path1[idx]

        path = distances.distance(self.solution,target, self.criteria)
        new_sol = path[min(self.v, len(path)-1)]

        #TODO: Add the apply_rarb function to pass through the target.
        # if self.v > len(target):
        #     n = self.v-len(target)
        #     for i in range(n):
        #         new_sol = utils.apply_rarb(self.solution)

        self.v = random.randint(1,10)
        self.solution = self.edit_solution(new_sol)

        return self.solution


def take_slice(l, first, end):
    r = random.randint(first+1, len(l)-end)
    return l[first:r]

def random_sol(clients):
    routes = random.randint(2,clients) #CHANGE 2 for 1!!!!
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
        particles.append(Particle(random_sol(clients)))
    return particles


def pso(clients, N=3, iterations = 3):
    part = init(clients, N)
    opt=None
    m, M = 10000, 0
    for ss in part:
        s = ss.solution
        m = min(m,len(s))
        M = max(M,len(s))
        if not opt or protocols.objective_function(s) < protocols.objective_function(opt):
            opt = [[c for c in r] for r in s]
    print(m)
    print(M)
    ch = False
    it = iterations
    while it > 0:
        for p in part:
            s = p.move(opt)
            if protocols.objective_function(s) < protocols.objective_function(opt):
                opt = [[c for c in r]for r in s]
                ch = True
        it-=1
    print(ch)
    return opt