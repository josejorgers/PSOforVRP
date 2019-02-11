from Distance import definitions

def split_criteria(self, criteria):

    chunks = criteria.split('r')

    result = []

    for c in chunks:
        inv, dep = 0,0

        for i in c:
            if i == 'a':
                dep += 1
            else:
                inv += 1
                dep -= 1
        result.append(definitions.CriteriaRoute(inv, dep))
    return result

class client_pos:
    def __init__(self, value, i, j):
        self.value = value
        self.i = i
        self.j = j

    def __hash__(self):
        return self.value

def make_set(destination):

    s = set()

    for i in range(len(destination)):
        for j in range(len(destination[i])):
            s.add(client_pos(destination[i][j], i, j))

def get_source(source, destination):

    src = []
    s = make_set(destination)

    for i in range(len(source)):
        src.append([])
        for j in range(len(source[i])):
#TODO: Learn about the python set and how to have the a structure which works as an AVL or a RedBlackTree
