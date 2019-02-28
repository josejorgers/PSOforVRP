import random, protocols
from Distance import distances, utils

class Particle:

    def __init__(self, solution, criteria = 'rarb'):
        self.solution = [[c for c in r] for r in solution]
        self.criteria = criteria
        self.own_best = [[c for c in r] for r in solution]
        self.v = random.randint(1,10)

    def get_distance_method(self):
        return distances.ab_distance

    def edit_solution(self,sol):

        if protocols.objective_function(sol) < protocols.objective_function(self.own_best):
            self.own_best = [[c for c in r] for r in sol]
        return [[c for c in r] for r in sol]

    def move(self, swarm_best):

        d_method = self.get_distance_method()

        d_pbest = len(d_method(self.solution, self.own_best))
        d_tbest = len(d_method(self.solution, swarm_best))

        ratio = d_tbest/(d_pbest + d_tbest)
        path1 = d_method(self.own_best, swarm_best)
        idx = int(ratio*len(path1))
        target = path1[idx]

        path = d_method(self.solution,target)
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
    sol = []
    first = 0
    for k in range(routes-1, 0, -1):
        slice = take_slice(l, first, k)
        sol.append(slice)
        first += len(slice)
    sol.append(l[first:])
    return sol


def init(clients, N):
    particles = []
    for s in range(N):
        particles.append(Particle(random_sol(clients)))
    return particles


def pso(clients, N=30, iterations = 20):
    part = init(clients, N)
    opt=None
    for ss in part:
        s = ss.solution
        if not opt or protocols.objective_function(s) < protocols.objective_function(opt):
            opt = [[c for c in r] for r in s]

    it = iterations
    while it > 0:
        for p in part:
            s = p.move(opt)
            if protocols.objective_function(s) < protocols.objective_function(opt):
                opt = [[c for c in r]for r in s]
        it-=1
    return opt