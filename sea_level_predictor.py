import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig = plt.figure(figsize = (10,6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    xpred= pd.Series([i for i in range(1880,2051)])
    ypred = res.slope*xpred + res.intercept
    plt.plot(xpred, ypred, color="green")

    # Create second line of best fit
    res = linregress(df['Year'][120:], df['CSIRO Adjusted Sea Level'][120:])
    xpred= pd.Series([i for i in range(2000,2051)])
    ypred = res.slope*xpred + res.intercept
    plt.plot(xpred, ypred, color="red")

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
