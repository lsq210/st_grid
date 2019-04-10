import os

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
    def load_samples(folder):
        all_files = os.listdir(folder)
        files = [x for x in all_files if '.csv' in x]
        index = 0
        for file_name in files:
            fp = open(folder + file_name, 'r')
            raw_data = fp.readlines()
            fp.close
            for row in raw_data:
                row_split = row.split()
                print(row_split)
                if row[3] == 0:
                    ST_GRID.samples.append(Sample(index, row[0], row[1], row[5], row[4]))
                    index += 1
        print(ST_GRID.samples)

    @staticmethod
    def plot_k_dist(k):
        pass

    @staticmethod
    def set_k(k):
        pass

    @staticmethod
    def solve():
        pass


