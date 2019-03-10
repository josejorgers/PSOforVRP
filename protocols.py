
matrix = None

demands = None

capacity = None

def objective_function(sol, penalty = 100):

    if not matrix  or not capacity:
        raise Exception('The "matrix" and "capacity" variables must be set')

    result = 0
    for r in sol:
        route_demand = sum([demands[c] for c in r])
        exceed = max(0, route_demand-capacity)
        result += penalty*exceed
        prev = 0
        for c in r:
            result += matrix[prev][c]
            prev = c
        result += matrix[prev][0]
    return result
