import requests
import json


url = "https://data.mongodb-api.com/app/data-ijmfb/endpoint/data/v1/action/aggregate"

querycategoryGroup = json.dumps(
  {
    "collection": "bikes",
    "database": "GreenMobility",
    "dataSource": "Cluster0",
    "pipeline": [{"$group": {"_id": "$category", "count": {"$sum":1}}}] })

    
headers = {
  'Content-Type': 'application/json',
  'Access-Control-Request-Headers': '*',
  'api-key': 'Hc28jQ1d3AefiXjJ0Z8xWdaL8OWc93aTTm8L2RuuhCh0ZADccNe4Hr6zEOerBM5o',
  'Accept': 'application/json' 
  }

category = requests.post(url, headers=headers, data=querycategoryGroup)
print(category.text)
