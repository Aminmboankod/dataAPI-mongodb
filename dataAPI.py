import requests
import json
url = "https://data.mongodb-api.com/app/data-iukxp/endpoint/data/v1/action/findOne"

payload = json.dumps({
    "collection": "bikes",
    "database": "DataAPItest",
    "dataSource": "Cluster0",
    "projection": {"name": 1, "_id": 0}
    
})
headers = {
  'Content-Type': 'application/json',
  'Access-Control-Request-Headers': '*',
  'api-key': 'TEQRZGzmpBJ8Ia3YgdEF8qrPrwQ6P9ayUlNLC710GvT2WrQqPNR0iEcARQ0GUwOj', 
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
