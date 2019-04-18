"""This module contains a collection of functions related to
 geographical data.

"""

from .utils import sorted_by_key  # noqa
from .stationdata import build_station_list
import numpy as np

def calculations(station_latitude,station_longitude,p):
    lat=station_latitude-p[0]
    lon=station_longitude-p[1]
    r=6371 #earth's radius
    d=2*r*np.arcsin(np.sqrt((np.sin(lat/2))**2+np.cos(station_latitude)*np.cos(p[0])*(np.sin(lon/2))**2))
    return d

def stations_by_distance(stations, p):
    distance=[]
    for station in stations:
        station_latitude=station.coord[0]/180*(np.pi) #taking coordinates out
        station_longitude=station.coord[1]/180*(np.pi)
        current_distance=(station, calculations(station_latitude,station_longitude,p))
        distance.append(current_distance)
    
    distance = sorted_by_key ( distance , 1)

    return distance

def stations_within_radius (stations, centre, r):
    within_radius=[]
    distance=stations_by_distance(stations, centre)
    for i in range (len(distance)):
        if distance[i][1]<=r:
            within_radius.append(distance[i][0].name)
    
    within_radius.sort()
    return within_radius

""" This modules reutrns a set of rivers around the stations"""

def rivers_with_station(stations):         
    river_names = set()                    #creates set 
    for station in stations:
        river_names.add(station.river)     #adds river name of each river in stations to set
    return river_names

""" This module returns a dictionary with keys of rivers and values of lists of stations on the river"""

def stations_by_river(stations):            
    river_names = rivers_with_station(stations)         #gets a set of the rivers in data
    list_of_empty_lists = []                            

    for i in range(len(river_names)):                   #creates a list of empyt lits
        list_of_empty_lists.append([])

    name_and_river = dict(zip(river_names,list_of_empty_lists))     #dictionary with keys of river names and values of empyt lists

    for station in stations:
        if station.river in river_names:
                name_list = name_and_river[station.river]
                name_list.append(station.name)
                sorted_name_list = sorted(name_list)
                name_and_river.update({station.river:sorted_name_list})
    return name_and_river

"""Function that returns a list of tuples, the first element containg the river name, the second, the number of statoins by it.
Takes the argument N which defines the least number of items in the list, as we include all with the same number of statoins as the last"""

def rivers_by_station_number(stations, N):
    river_and_stations_dict = stations_by_river(stations)                           #creates dictionary with key of river and list of stations
    river_and_stations_list = map(list, river_and_stations_dict.items())            #creats a list of keys and values as one item
    list_of_rivers_and_no_stations = []                                             
    for entry in river_and_stations_list:
        temp_var = len(entry[1])                                                    #stores the length of the list of statoins by the river
        temp_var = (entry[0],temp_var)        
        list_of_rivers_and_no_stations.append(temp_var)                             #appends tuple to empty list making list of river and number of staions
    sorted_rivers_no_stations = sorted(list_of_rivers_and_no_stations, key=lambda x: x[1], reverse=True)    #sorts list by number of stations in tuple
    sorted_limited_list = sorted_rivers_no_stations[:N]                             #slices sorted list so only first N elements are present
    counter = 0 
    for item in sorted_rivers_no_stations[N:]:                                      #this loop adds the elements with same number of stations
        station_river_tup = sorted_limited_list[-1]
        if item[1] == station_river_tup[1]:
            sorted_limited_list.append(item)
        else:
            break
        counter +=1
    return(sorted_limited_list)
