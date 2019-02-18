
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