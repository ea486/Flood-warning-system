from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius
import numpy as np

def test_stations_within_radius():
    stations=build_station_list()
    given_latitude=52.2053/180*(np.pi)
    given_longitude=0.1218/180*(np.pi)
    centre=[given_latitude,given_longitude]
    r = 1 #radius
    station_in_radius=stations_within_radius(stations,centre, r)
    assert station_in_radius==['Cambridge Jesus Lock']