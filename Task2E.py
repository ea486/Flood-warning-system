import datetime
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_levels
from floodsystem.flood import stations_highest_rel_level

"""Task 2E: plot water level"""

def run():
    # Build list of stations
    stations = build_station_list()
    N=5
    update_water_levels(stations)
    list_of_5_stations_greatest_level=stations_highest_rel_level(stations , N)
    dt=10
    for station in list_of_5_stations_greatest_level:
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        plot_water_levels(station, dates, levels)
   

if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()
