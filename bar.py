#Set up graph: Bar graph comparing base stats of Empoleon

#import csv, requests for API, panda, and bokeh
import csv
import requests
import pandas as pd
from bokeh.charts import Bar, output_file, save
from bokeh.layouts import row

#Open csv file and create csv writer
file = open("stats.csv","w")
csv = csv.writer(file,delimiter = ",")

#write to file
#hit points, attack, defense, special attack, special defense, speed
csv.writerow(["stats","base"])

#Set up URL for API
#get the name and every stat for empoleon
empoleon = 395
endpoint = "http://pokeapi.co/api/v2/"
num = "pokemon/"+str(empoleon)+"/"
url = endpoint+num
payload = {}
    
#send request and check status
r = requests.get(url, params=payload)
print(r)

#find each base stat and set it to a variable
dex = r.json()
speed = dex["stats"][0]["base_stat"]
spd = dex["stats"][1]["base_stat"]
spa = dex["stats"][2]["base_stat"]
df = dex["stats"][3]["base_stat"]
att = dex["stats"][4]["base_stat"]
hp = dex["stats"][5]["base_stat"]

#write rows containing each stat in order
csv.writerow(["hp",hp])
csv.writerow(["attack",att])
csv.writerow(["defense",df])
csv.writerow(["special attack",spa])
csv.writerow(["special defense",spd])
csv.writerow(["speed",speed])

#close file
file.close()

#give csv file for bokeh to read
emdata = pd.read_csv("stats.csv")


#Create a bar plot using bokeh
bar = Bar(emdata, values="base", label="stats", title="Empoleon Base Stats")

#Create graph file
output_file("bar.html")
save(bar)
print("complete")

