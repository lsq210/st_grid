from operator import itemgetter
from datetime import datetime
from itertools import groupby
import os
import math
import matplotlib.pyplot as plt

EARTH_RADIUS = 6371  # 地球平均半径，6371km
C = 66 #时间间隔前的系数

class Sample(object):
    id = -1
    date = None
    time = None
    lat = 0
    lng = 0
    k_distance = -1 
 
    def __init__(self, id, date, time, lat, lng, k_distance=0):
        (self.id, self.date, self.time, self.lat, self.lng, self.k_distance) = (id, date, time, lat, lng, k_distance)

class ST_GRID:
    samples = []
    k = 0

    @staticmethod
    def init():
        ST_GRID.samples = []
        k = 4

    @staticmethod
    def load_samples(path):
        index = 0
        file = open(path, 'r')
        raw_data = file.readlines()
        file.close
        for row in raw_data:
            row_split = row.split()
            if row_split[3] == '0.0':
                ST_GRID.samples.append(Sample(index, row_split[0], row_split[1], float(row_split[5]), float(row_split[4])))
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
            for t in test[0:2]:
                print(str(t.id) + ' ' + t.date + ' ' + str(t.lng) + ' ' + str(t.lat) + ' ' + str(t.k_distance))
            print('\n\n')

     
    @staticmethod   
    def hav(theta):
        s = math.sin(theta / 2)
        return s * s

    @staticmethod
    def get_st_distance(sample0, sample1):
        # "用haversine公式计算球面两点间的距离。返回单位为米
        # 经纬度转换成弧度
        lat0 = math.radians(sample0.lat)
        lat1 = math.radians(sample1.lat)
        lng0 = math.radians(sample0.lng)
        lng1 = math.radians(sample1.lng)

        dlng = math.fabs(lng0 - lng1)
        dlat = math.fabs(lat0 - lat1)
        h = ST_GRID.hav(dlat) + math.cos(lat0) * math.cos(lat1) * ST_GRID.hav(dlng)
        distance = 2 * 1000 * EARTH_RADIUS * math.asin(math.sqrt(h))
        t0 = datetime.strptime(sample0.date + ' ' + sample0.time, "%Y-%m-%d %H:%M:%S").second
        t1 = datetime.strptime(sample1.date + ' ' + sample1.time, "%Y-%m-%d %H:%M:%S").second
        st_distance = math.sqrt(distance * distance + C * (t0 - t1) * (t0 - t1))
        return st_distance
    
    @staticmethod
    def sovle_k_distance():
        # n = 0
        for group in ST_GRID.samples:
            for i in range(len(group)):
                st_distance_list = []
                for j in range(len(group)):
                    if j - i > 120 or i == j:
                        continue
                    st_distance = ST_GRID.get_st_distance(group[i], group[j])
                    st_distance_list.append(st_distance)
                    # n =  n + 1                  
                    # if n % 1000 == 0:
                    #     print("{} \n".format(n/1000))
                st_distance_list.sort(reverse = False)
                group[i].k_distance = st_distance_list[ST_GRID.k-1] 
    
    @staticmethod
    def plot_k_dist():
        k_dist_list = []
        x = []
        for group in ST_GRID.samples:
            for sample in group:
                k_dist_list.append(sample.k_distance)
                x.append(sample.id)
        k_dist_list.sort(reverse = True)
        plt.scatter(k_dist_list, x)
        plt.show()

    @staticmethod
    def set_k(k):
        pass

    @staticmethod
    def solve():
        pass


