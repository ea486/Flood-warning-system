from floodsystem.analysis import polyfit
from floodsystem.plot import plot_water_level_with_fit
import numpy as np
import datetime
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import *

"""Task 2F: function fitting"""

def run():
    # Build list of stations
    stations = build_station_list()
    N=5 #number of stations we consider of having highest risk of flood
    update_water_levels(stations)
    list_of_5_stations_greatest_level=stations_highest_rel_level(stations , N)
    dt=2
    p=4 #degree 4 against time
    for station in list_of_5_stations_greatest_level:
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        poly, d0 = polyfit(dates, levels, p)
        plot_water_level_with_fit(station, dates, levels, p)

if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()
