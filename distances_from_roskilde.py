
import pandas as pd
import os,math,platform
import csv

if platform.system() == 'Windows':
    newline = ''
else:
    newline = None



def haversine_distance(origin, destination):

    lat_orig, lon_orig = origin
    lat_dest, lon_dest = destination
    radius = 6371

    dlat = math.radians(lat_dest-lat_orig)
    dlon = math.radians(lon_dest-lon_orig)
    a = (math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(math.radians(lat_orig))
        * math.cos(math.radians(lat_dest)) * math.sin(dlon / 2) * math.sin(dlon / 2))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = radius * c

    return d

csv_geo =csv.reader(open('boliga_all_detailed_lon_lat.csv', newline=newline));


for i,row in enumerate(csv_geo):
    if i==0:
        continue
    if row.__len__()>15:
        end_point = (float(row[15]),float(row[16]))
        print( haversine_distance((55.65,12.083333),end_point))