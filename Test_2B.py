from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import *

def test_stations_level_over_thresholds():
    stations=build_station_list()
    update_water_levels(stations)
    stations = stations[:100] #Make sure no none types here
    for station in stations:
        assert station.relative_water_level(station) > -100 and station.relative_water_level(station) < 100


def test_stations_level_over_thresholds():
    stations=build_station_list()
    update_water_levels(stations)
    stations = stations[:10] #Make sure no none types here
    stations_over = stations_level_over_threshold(stations,-1000)
    assert len(stations_over) == len(stations)
    station_over = stations_level_over_threshold(stations,1000)
    assert len(station_over) == 0