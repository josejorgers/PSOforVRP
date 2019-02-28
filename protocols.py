
def objective_function(sol):

    solve = 0
    for r in range(len(sol)):
        solve += (r+1)*len(sol[r])
    return solve