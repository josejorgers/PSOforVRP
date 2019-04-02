from Distance import  swap_distance, ab_distance, subroute_distance

distances = {
    'rarb' : ab_distance.distance,
    'rarac' : swap_distance.distance,
    'rdre' : subroute_distance.distance#subroute_distance.distance
}

def distance(source, destination, criteria):
    return distances[criteria](source, destination)
