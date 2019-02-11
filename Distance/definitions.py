
class Route:

    def __init__(self, departures, inversions):

        self.departures = departures
        self.inversions = inversions


class Client:

    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


class CriteriaRoute:

    def __init__(self, inversions, departures):

        self.inversions = inversions
        self.departures = departures
        self.tmp_inv = inversions
        self.tmp_dep = departures


    def make_inversion(self):
        self.tmp_inv-=1

    def make_departure(self):
        self.tmp_dep-=1

    @property
    def get_departures(self):
        return self.tmp_dep

    @property
    def get_inversions(self):
        return self.tmp_inv

    def restart(self):
        self.tmp_dep = self.departures
        self.tmp_inv = self.inversions