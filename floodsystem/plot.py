"This module contains the main functions to plot the data"
import matplotlib
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from .analysis import polyfit
def plot_water_levels(station, dates, levels):

# Plot
    plt.plot(dates, levels)
    typical_high=station.typical_range[1]
    typical_low=station.typical_range[0]
    high=[]
    low=[]
    length_dates=len(dates)
    for i in range (length_dates):
        high.append(typical_high)
        low.append(typical_low)
    plt.plot(dates, high)
    plt.plot(dates, low)
# Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)
    
# Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()

def plot_water_level_with_fit(station, dates, levels, p):
    poly, d0 =polyfit(dates,levels,p)
    typical_high=station.typical_range[1]
    typical_low=station.typical_range[0]
    high=[]
    low=[]
    length_dates=len(dates)
    for i in range (length_dates):
        high.append(typical_high)
        low.append(typical_low)
    plt.plot(dates, high)
    plt.plot(dates, low)
    plt.plot(matplotlib.dates.date2num(dates),levels)
    plt.plot (dates, poly(matplotlib.dates.date2num(dates)-d0))
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(station.name)
    plt.show()