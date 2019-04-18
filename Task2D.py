# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

import datetime
from floodsystem.stationdata import build_station_list
from floodsystem.datafetcher import fetch_measure_levels

"""Task 2D: level data time history"""

def run():

    # Build list of stations
    stations = build_station_list()

    # Find station 'Cam'
    for station in stations:
        if station.name == 'Cam':
            station_cam = station
            break

    # Fetch data over past 2 days
    dt = 2
    dates, levels = fetch_measure_levels(station_cam.measure_id,
                                         dt=datetime.timedelta(days=dt))

    # Print level history
    for date, level in zip(dates, levels):
        print(date, level)

if __name__ == "__main__":
    print("*** Task 2D: CUED Part IA Flood Warning System ***")
    run()
