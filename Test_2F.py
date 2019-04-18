import matplotlib
import matplotlib.pyplot as plt
from floodsystem.analysis import polyfit
import datetime
from floodsystem.stationdata import build_station_list
from floodsystem.datafetcher import fetch_measure_levels

def test_polyfit(): 
    stations = build_station_list()
    
    list_of_5_stations_random=[]
    p=0
    for station in stations:
        list_of_5_stations_random.append(station)
        p=p+1
        if p==5:
            break
    dt=2
    p=4 #degree 4 against time
    for station in list_of_5_stations_random:
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        poly, d0 = polyfit(dates, levels, p)
    assert isinstance(poly, tuple)==True