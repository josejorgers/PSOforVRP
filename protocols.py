def objective_function(sol):

    solve = 0
    for r in range(len(sol)):
        solve += (r+1)*sum(sol[r])
    return solve