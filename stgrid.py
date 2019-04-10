#!/usr/bin/python
# -*- coding: utf-8 -*-

from datetime import timedelta
import math
import numpy as np
EARTH_RADIUS = 6371  # 地球平均半径，6371km

def hav(theta):
    s = math.sin(theta / 2)
    return s * s


def get_distance_hav(lat0, lng0, lat1, lng1):
    #    "用haversine公式计算球面两点间的距离。返回单位为米
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

class STGRID(object):

    