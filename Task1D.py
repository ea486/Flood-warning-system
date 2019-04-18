
from floodsystem.stationdata import build_station_list
from floodsystem.geo import *

"""Task 1D: rivers with a station(s)"""

def run():
    stations = build_station_list()
    rivers = list(rivers_with_station(stations))    
    sorted_rivers = sorted(rivers)
    print("Number of river with at least one station: {} \n".format(len(rivers)))
    print("first 10 rivers: ", sorted_rivers[:10],"\n")
    river_names = ["River Aire", "River Cam", "River Thames"]   
    river_station_dict = stations_by_river(stations)
    for river_name in river_names:
        station_names_list = river_station_dict[river_name]
        sorted_station_name_list = sorted(station_names_list)
        print("Stations by river: ", river_name, " : " , sorted_station_name_list,"\n")

if __name__ == "__main__":
    run()



