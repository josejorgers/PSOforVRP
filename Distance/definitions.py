
class Route:

    def __init__(self, inversions, departures, insertions):

        self.inversions = inversions
        self.departures = departures
        self.insertions = insertions
        self.tmp_inv = inversions
        self.tmp_dep = departures
        self.tmp_insert = insertions


    def make_inversion(self):
        self.tmp_inv-=1

    def make_departure(self):
        self.tmp_dep-=1

    def make_insertion(self):
        self.tmp_insert-=1

    @property
    def get_departures(self):
        return self.tmp_dep

    @property
    def get_inversions(self):
        return self.tmp_inv

    @property
    def get_insertions(self):
        return self.tmp_insert

    def restart(self):
        self.tmp_dep = self.departures
        self.tmp_inv = self.inversions
        self.tmp_insert = self.insertions

class ClientRoute(Route):

    def __init__(self, inversions, departures, insertions, depart_queue, inv_queue, changes_dict):

        super(ClientRoute, self).__init__(inversions, departures, insertions)
        self.dep_queue = depart_queue
        self.inv_queue = inv_queue
        self.dict = changes_dict
        self.changes = []

    def make_inversion(self):

        if self.tmp_inv > 0:
            self.tmp_inv-=1
            client = self.inv_queue.get_nowait()
            self.changes.append((self.dict[client], client))

    def make_departure(self):

        if self.tmp_dep > 0:
            self.tmp_dep -= 1
            client = self.dep_queue.get_nowait()
            self.changes.append((self.dict[client], client))
            return client
    def clean_changes(self):
        self.changes = []
