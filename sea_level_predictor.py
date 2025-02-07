import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    data = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots(figsize = (10,5), dpi = 100)
    plt.scatter(data = data, x = "Year", y = "CSIRO Adjusted Sea Level") 
    # Create first line of best fit
    filt1 = linregress(data["Year"], data["CSIRO Adjusted Sea Level"])
    extended_years = range(min(data["Year"]), 2051)
    y_pred = filt1.intercept + filt1.slope * extended_years
    plt.plot(extended_years, y_pred, color="yellow")
    # Create second line of best fit
    if  data["CSIRO Adjusted Sea Level"].loc[data["Year"] >= 2000].mean() > data["CSIRO Adjusted Sea Level"].loc[data["Year"] == 2000].values[0]:
        data2 = data.loc[data["Year"] >= 2000]
        filt2 = linregress(data2["Year"], data2["CSIRO Adjusted Sea Level"])
        best_fit= range(2000,2051)
        y_pred2 = filt2.intercept + filt2.slope * best_fit
        plt.plot(best_fit, y_pred2, color ="red") 
    # Add labels and title
    plt.xlabel("Year")   
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()