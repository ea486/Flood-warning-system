from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations

"""Task 1F: typical low/high range consistency"""


def run():
    # Build list of stations
    stations = build_station_list()
    print (inconsistent_typical_range_stations(stations))

if __name__ == "__main__":
    run()