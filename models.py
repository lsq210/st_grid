from operator import itemgetter
from itertools import groupby
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
    def init():
        ST_GRID.samples = []
        k = 0

    @staticmethod
    def load_samples(path):
        index = 0
        file = open(path, 'r')
        raw_data = file.readlines()
        file.close
        for row in raw_data:
            row_split = row.split()
            if row_split[3] == '0.0':
                ST_GRID.samples.append(Sample(index, row_split[0], row_split[1], row_split[5], row_split[4]))
                index += 1
        ST_GRID.samples = ST_GRID.groupby(ST_GRID.samples)
    
    @staticmethod
    def groupby(samples):
        groups = []
        for sample in samples:
            need_new_group = True
            for group in groups:
                if group[0].date == sample.date:
                    group.append(sample)
                    need_new_group = False
            if need_new_group:
                new_group = [sample,]
                groups.append(new_group)
        return groups
    
    @staticmethod
    def print_samples():
        for test in ST_GRID.samples:
            for t in test[0:20]:
                print(str(t.id) + ' ' + t.date + ' ' + str(t.lng) + ' ' + str(t.lat))
            print('\n\n')
        print('days {}'.format(len(ST_GRID.samples)))

        
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


