import matplotlib
import matplotlib.pyplot as plt

def test_plotting_graphs(): 
    name = "test station"
    dates=["2012","2013","2014"]
    levels=[1.01,1.04,1.02]
    plt.plot(dates, levels)

# Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(name)
    plt.show()
    assert plt.plot.called
    
