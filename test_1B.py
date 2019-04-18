from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list
import numpy as np

def test_stations_by_distance():

     # Build list of stations
    stations = build_station_list()
    given_latitude=52.2053/180*(np.pi)
    given_longitude=0.1218/180*(np.pi)
    p=[given_latitude,given_longitude]
    distance=stations_by_distance(stations,p)
    test_list=[]
    for i in range (len(distance)):
        x=(distance[i][0].name, distance[i][0].town, distance[i][1])
        test_list.append(x)

    assert test_list[0]==('Cambridge Jesus Lock', 'Cambridge', 0.8402364350834995)