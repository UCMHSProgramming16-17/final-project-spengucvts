#Set up graph: Scatter plot for speed stat of all Gen 4 Pokemon

#import csv, requests for API, panda, and bokeh
import csv
import requests
import pandas as pd
from bokeh.charts import Scatter, output_file, save
    
#Open csv file and create csv writer
file = open("speed.csv","w")
csv = csv.writer(file,delimiter = ",")

#write to file
#id, name, weight
csv.writerow(["dex number", "name", "speed"])

#Use for-loop to run through every Gen 4 pokemon and return the data
gen4 = range(387,494)
for id in gen4:
    
    #Set up URL for API
    #get the name and speed for each dex number/id
    endpoint = "http://pokeapi.co/api/v2/"
    num = "pokemon/"+str(id)+"/"
    url = endpoint+num
    payload = {}
    
    #send request and check status
    r = requests.get(url, params=payload)
    
    #Find the name in the dictionary and set it to a variable
    dex = r.json()
    name = dex["name"]
    
    #find the speed for each pokemon and set it to a variable
    stats = dex["stats"]
    speed = dex["stats"][0]["base_stat"]
    
    #write a row containing the dex number/id, name, and weight in that order
    csv.writerow([id, name, speed])

#close file
file.close()

#give csv file for bokeh to read
scdata = pd.read_csv("speed.csv")

#Create a scatter plot using bokeh + import scatter
#Add a hovering legend that gives the name and dex number and base speed if you hover over a dot
from bokeh.models import HoverTool
legend = "hover"
scatter=Scatter(scdata,title="Gen 4 Pokemon Base Speed", x="dex number",y="speed",xlabel="Pokemon Dex Number", ylabel="Pokemon Base Speed", tools = legend)
output_file("scatter.html")
save(scatter)
print("complete")

