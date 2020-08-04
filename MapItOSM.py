APIKEY = "GetYourOwn"
import pprint
import csv
import json
import requests
import pandas as pd
import time

pp = pprint.PrettyPrinter(indent=4)
settlements = []
def main():
    with open('OSM.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        wikiline = {}
        for row in reader:
            expectedresponse = {
                    "item": "", 
                    "placetype":"",
                    "coords":"",
                    "Scottish Parliament region":"",
                    "Scottish Parliament constituency":"",
                    "UK Parliament constituency":"",
                    "Scottish Health Board":"",
                    "Unitary Authority ward (UTW)":"",
                    "Unitary Authority":"",
                    "European region":""
                }
            item = row['name']
            coords = [row['@lon'],row['@lat']]
            placetype = row['place']
            if (coords):
                time.sleep(1.5)
                #coords = coords.split("Point(")[1].replace(")","").split(" ")
                APIquery = "point/4326/" + coords[0] + "," + coords[1]
                response = requests.get("https://mapit.mysociety.org/"+APIquery+"?api_key="+APIKEY)
                try:
                    response = json.loads(response.content)
                except:
                    print('failed - waiting 5 sec')
                    time.sleep(5)
                    try:
                        response = requests.get("https://mapit.mysociety.org/"+APIquery+"?api_key="+APIKEY)
                        response = json.loads(response.content)
                    except:
                        print('failed - give up')
                        response = {}
                #pp.pprint(response)
                for r in response:
                    for er in expectedresponse:
                        if response[r]["type_name"] == er:
                            expectedresponse[er] = response[r]["name"]
            else:
                coords = ""
            expectedresponse["item"] = item
            expectedresponse["coords"] = coords
            expectedresponse["placetype"] = placetype
            response = expectedresponse
            wikiline = response
            pp.pprint(item)
            settlements.append(wikiline)

        pp.pprint(settlements)
        with open('c:/Users/gav_b/GitHub/WikiTools/jsonout.json', 'w') as f:
            json.dump(settlements, f)
        df = pd.read_json('c:/Users/gav_b/GitHub/WikiTools/jsonout.json')
        df.to_csv('pandaout.csv', header=True)
        print("Done!")

main()