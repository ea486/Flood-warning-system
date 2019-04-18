from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import *

def test_stations_level_over_thresholds():
    stations=build_station_list()
    update_water_levels(stations)
    stations = stations[:10] #Make sure no none types here
    riskiest_stations = stations_highest_rel_level(stations, 10)
    assert len(riskiest_stations) == 10