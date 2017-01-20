#import csv, requests for API, panda, scatter plot, and bokeh
import csv
import requests
import pandas as pd
from bokeh.charts import Scatter, output_file, save
from bokeh.models import HoverTool, ColumnDataSource

#give csv file for bokeh to read
scdata = pd.read_csv("speed.csv")

#Add a hovering legend that gives the name and dex number and base speed if you hover over a dot
#Create a scatter plot using bokeh
legend = "hover"

source = ColumnDataSource(
  data = dict(
      x=scdata['dex number'],
      y=scdata['speed'],
      name=scdata['name'],
     )    
    )
    
scatter=Scatter(scdata,title="Gen 4 Pokemon Base Speed", 
    x="dex number",
    y="speed",
    xlabel="Pokemon Dex Number", 
    ylabel="Pokemon Base Speed", 
    tools=legend, source=source)

#Create hovering legend
hover = scatter.select(dict(type=HoverTool))
hover.point_policy = "follow_mouse"
hover.tooltips=[
    ("Name", "@name"),
    ("Dex Number", "@x"),
    ("Base Speed", "@y"),
]

     
#Create graph file
output_file("scatter.html")
save(scatter)
print("complete")