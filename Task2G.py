from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.analysis import polyfit
from floodsystem.plot import plot_water_level_with_fit
import datetime
import numpy as np

"""Task 2G: issuing flood warnings for towns"""
    

def evaluate_risk(station,gradient_weight,time_weight,height_weight):

    dt=2
    p=4 #degree 4 against time
    risk_level = 0
    dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
    try:   #Tries to see if there is data and can fit a polynomial to it
        data_consistent = True
        poly, d0 = polyfit(dates, levels, p)
        gradient = np.gradient(poly)
        risk_level += gradient_weight*gradient[-1]
        if gradient[:1] > 0:
                gradient2 =  list(np.gradient(gradient)) 
                gradient2.reverse()
                try: #tries to find lenght of time that the water has been rising
                        index_min = gradient.index(0)
                        risk_level += (len(gradient) - index_min)*time_weight
                except:
                        pass
        risk_level += station.relative_water_level()*height_weight
    except:
            data_consistent = False
    return risk_level,data_consistent




def print_risk_level(station_list):
#This function takes in the risk number and quantieses it'''
     risk_level = ""
     for station in station_list:
        risk_level = "No data"
        if station[1] <100:
                risk_level = "SEVERE"
        if station[1] <1.5:
                risk_level = "HIGH"
        if station[1] < 1.1:
                risk_level = "MODERATE"
        if station[1] <0.5:
                risk_level = "LOW"
        print(station[0],risk_level)
     return station_list

def run():
    risk_list = []
    stations = build_station_list()
    stations = stations[:100]               #Splice the stations, just for testing as all stations takes a very long time
    update_water_levels(stations)



#    incosistend_stations = inconsistent_typical_range_stations(stations)  #creates a list of stations with inconsistent data
#    stations = [x for x in stations if x not in incosistend_stations]

    for station in stations:
            risk_level,data_good = evaluate_risk(station,1,0.002,5)
            risk_tuple = (station.name,risk_level)
            if data_good == True:
                risk_list.append(risk_tuple)
            else:
                risk_list.append((station.name,100000)) 
    risk_list.sort(key=lambda x: x[1], reverse=True)
    print_risk_level(risk_list)
    

if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()

