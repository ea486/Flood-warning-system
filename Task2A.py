from floodsystem.stationdata import build_station_list, update_water_levels

"""Task 2A: fetch real-time river levels"""

def run():
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    # Print station and latest level for first 5 stations in list
    names = [
        'Bourton Dickler', 'Surfleet Sluice', 'Gaw Bridge', 'Hemingford',
        'Swindon'
    ]
    for station in stations:
        if station.name in names:
            print("Station name and current level: {}, {}".format(
                station.name, station.latest_level))



if __name__ == "__main__":
    print("*** Task 2A: CUED Part IA Flood Warning System ***")
    run()
