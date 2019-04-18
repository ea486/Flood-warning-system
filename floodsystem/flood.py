"This module contains the main functions to asses the flood situation of stations"

def stations_level_over_threshold(stations, tol):
    """Returns a list of stations which have a relative water level higher then a tolerence, returns nothing if there is a none type in the relative water level"""
    stations_over_limit = []
    for station in stations:
        try:
            if  station.relative_water_level() > tol:
                stations_over_limit.append((station.name,station.relative_water_level()))
        except:
            pass
    stations_over_limit.sort(key=lambda x: x[1], reverse=True)
    return stations_over_limit

def stations_highest_rel_level(stations, N):
    '''Returns a list of N lenght of the stations with the highest relative water level'''
    full_list = []
    for station in stations:
        if station.relative_water_level() != None:
            full_list.append(station)
        else:
            break
    
    full_list.sort(key=lambda x: x.relative_water_level(), reverse = True)
    return full_list[:N]