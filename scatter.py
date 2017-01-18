#Set up graph: Scatter plot for speed stat of all Gen 4 Pokemon

#import csv and requests for API
import csv
import requests
    
#Open csv file and create csv writer
file = open("speed.csv","w")
csv = csv.writer(file,delimiter = ",")

#write to file
#id, name, weight
csv.writerow(["dex number", "name", "speed"])

#Use for-loop to run through every Gen 4 pokemon and return the data
#gen4 = range(387,494)
gen4 = range(1,2)
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
    
    #find the speed for each pokemon and set it to a variable
    stats = dex["stats"]
    speed = dex["stats"][0]["base_stat"]
    
    #write a row containing the dex number/id, name, and weight in that order
    csv.writerow([id, name, speed])

#close file
file.close()