import requests
import json


url = "https://data.mongodb-api.com/app/data-ijmfb/endpoint/data/v1/action/aggregate"



queryAllbikes = json.dumps(
   {
     "collection": "bikes",
     "database": "GreenMobility",
     "dataSource": "Cluster0",
     "projection": {"name":1, "_id": 0, "category": 1}
     })
    
headers = {
  'Content-Type': 'application/json',
  'Access-Control-Request-Headers': '*',
  'api-key': 'Hc28jQ1d3AefiXjJ0Z8xWdaL8OWc93aTTm8L2RuuhCh0ZADccNe4Hr6zEOerBM5o',
  'Accept': 'application/json' 
  }

name = requests.post(url, headers=headers, data=queryName)
print(name.text)


response = requests.post(url, headers=headers, data=queryAllbikes)
print(response.text)