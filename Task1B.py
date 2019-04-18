from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance
import numpy as np

"""Task 1B: sort stations by distance"""

def run():
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
    print(test_list[:10])
    print(test_list[-10:])

if __name__ == "__main__":
    run()