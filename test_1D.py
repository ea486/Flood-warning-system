from floodsystem.stationdata import build_station_list
from floodsystem.geo import *


def test_rivers_with_station(): 
    stations = build_station_list()
    stations = stations[15:35]
    rivers = rivers_with_station(stations)
    
    assert len(rivers) == 19
    assert isinstance(rivers, set) == True

def test_stations_by_rver():
    stations = build_station_list()
    stations = stations[15:35]
    river_stat_dict = stations_by_river(stations)
    assert isinstance(river_stat_dict, dict) == True
    assert river_stat_dict['River Wharfe'] == ['Addingham, Town Beck', 'Fleet Pumping Station']

    

