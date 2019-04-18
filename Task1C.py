from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius
import numpy as np

"""Task 1C: stations within radius"""

def run():
    # Build list of stations
    stations = build_station_list()
    given_latitude=52.2053/180*(np.pi)
    given_longitude=0.1218/180*(np.pi)
    centre=[given_latitude,given_longitude]
    r = 10 #radius
    print(stations_within_radius(stations,centre, r))
    

if __name__ == "__main__":
    run()