#Set up graph: Pie chart for all Gen 4 water types

#import csv, requests for API, panda, and bokeh
import csv
import requests
import pandas as pd
from bokeh.charts import Donut, output_file, save

#Open csv file and create csv writer
file = open("water.csv","w")
csv = csv.writer(file,delimiter = ",")

#write to file
#id, name, weight
csv.writerow(["id", "name", "type1","type2"])

#Use for-loop to run through every Gen 4 pokemon and return the data
#gen4 = range(387,494)
gen4 = range(1,5)
for id in gen4:
    
    #Set up URL for API
    #get the name and speed for each dex number/id
    endpoint = "http://pokeapi.co/api/v2/"
    num = "pokemon/"+str(id)+"/"
    url = endpoint+num
    payload = {}
    
    #send request and check status
    r = requests.get(url, params=payload)
    print(r)
    
    #Find the name in the dictionary and set it to a variable
    dex = r.json()
    name = dex["name"]
    
    #find the type for each pokemon and set it to a variable
    type = dex["types"]
    type1 = dex["types"][0]["type"]["name"]
    
    #If statement is accounting for dual-types
    #write a row containing the dex number/id, name, and weight in that order
    if len(type) == 2:
        type2 = dex["types"][1]["type"]["name"]
        csv.writerow([id, name, type1, type2])
    else:
        csv.writerow([id, name, type1, "none"])

#close file
file.close()

#give csv file for bokeh to read
pdata = pd.read_csv("water.csv")


#Create a pie chart using bokeh
p = Donut(pdata, label=['id'], values='type1',
          text_font_size='8pt', hover_text='medal_count')

output_file("pie.html")

show(d)