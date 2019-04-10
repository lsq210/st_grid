import os
import math
EARTH_RADIUS = 6371  # 地球平均半径，6371km
C = 66 #时间间隔前的系数

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
                # print(row_split)
                if row_split[3] == '0.0':
                    ST_GRID.samples.append(Sample(index, row[0], row[1], row[5], row[4]))
                    index += 1
        # print(ST_GRID.samples)
    
    def hav(theta):
        s = math.sin(theta / 2)
        return s * s

    def get_distance(lat0, lng0, lat1, lng1):
        # "用haversine公式计算球面两点间的距离。返回单位为米
        # 经纬度转换成弧度
        lat0 = math.radians(lat0)
        lat1 = math.radians(lat1)
        lng0 = math.radians(lng0)
        lng1 = math.radians(lng1)

        dlng = math.fabs(lng0 - lng1)
        dlat = math.fabs(lat0 - lat1)
        h = hav(dlat) + math.cos(lat0) * math.cos(lat1) * hav(dlng)
        distance = 2 * EARTH_RADIUS * math.asin(math.sqrt(h))
        return distance * 1000
    
    def  get_st_distance():
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


