from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold

"""Task 2B: assess flood risk by level"""

def run():
    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)
    stations_over_limit = stations_level_over_threshold(stations,0.8)
    for station in stations_over_limit:
        print(station)

if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()
