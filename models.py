class Sample(object):
    id = -1
    date = None
    time = None
    lat = 0
    lng = 0
    k_distance = 0 
 
    def __init__(self, id, date, time, lat, lng, k_distance=0):
        (self.id, self.date, self.time, self.lat, self.lng, self.k_distance) = (id, date, time, lat, lng, k_distance)

class ST_GRID:
    samples = []
    k = 0

    @staticmethod
    def load_samples(path):
        pass
    
    @staticmethod
    def plot_k_dist(k):
        pass

    @staticmethod
    def set_k(k):
        pass

    @staticmethod
    def solve():
        pass


