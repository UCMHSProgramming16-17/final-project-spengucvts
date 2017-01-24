#import csv, requests for API, panda, scatter plot, and bokeh
import csv
import requests
import pandas as pd
from bokeh.charts import Scatter, output_file, save
from bokeh.models import HoverTool, ColumnDataSource

#give csv file for bokeh to read
scdata = pd.read_csv("speed.csv")
print(list(scdata.columns.values))

#Add a hovering legend that gives the name and dex number and base speed if you hover over a dot
legend = "hover"
source = ColumnDataSource(data=scdata)

#Create a scatter plot using bokeh
scatter=Scatter(scdata,title="Gen 4 Pokemon Base Speed", 
    x="dex number",
    y="speed",
    xlabel="Pokemon Dex Number", 
    ylabel="Pokemon Base Speed", 
    tools=legend, source=source)
scatter.circle('dex number', 'speed', "name", size=10, source=source)

#Create hovering legend
hover = scatter.select(dict(type=HoverTool))
hover.tooltips= ([("Name", "@{name}"), ("Dex Number", "@{dex number}"), ("Base Speed", "@speed"),])

#Create graph file
output_file("scatter.html")
save(scatter)
print("complete")
