from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number

def test_rivers_by_station_number(): 
    stations = build_station_list()
    tuple_list = rivers_by_station_number(stations, 50)
    assert isinstance(tuple_list,list) == True
    assert isinstance(tuple_list[0], tuple) == True
    i = 0
    for i in range(len(tuple_list)-1):
        assert tuple_list[i][1] >= tuple_list[i+1][1]
    assert len(tuple_list) == 60