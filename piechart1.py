#import csv, requests for API, panda, and bokeh
import csv
import requests
import pandas as pd
from bokeh.charts import Donut, output_file, save

#give csv file for bokeh to read
pdata = pd.read_csv("water.csv")

#Count values for each type
#Find the number of water types (primary or secondary)
#Find total number of pokemon in Gen 4
#Calculate percentage of watertypes
t1 = pdata['type1'].value_counts().to_dict()
t2 = pdata["type2"].value_counts().to_dict()
total = len(pdata.index) - 1
w = t2["water"]+t1["water"]
wpercent = total/w
opercent = 1 - wpercent
index = ["water", "nonwater"]
color = ["cyan","gray"]

#Create a pie chart using bokeh
data = pd.Series([wpercent,opercent], index = list(index))
p = Donut(data, color = list(color), title = "Percentage of Water Types in Gen 4")

output_file("pie.html")

save(p)