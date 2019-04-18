from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import *

"""Task 2C: most at risk stations"""

def run():
    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)
    risky_stations = stations_highest_rel_level(stations,10)
    for station in risky_stations:
        print(station.name, station.relative_water_level())

if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()
