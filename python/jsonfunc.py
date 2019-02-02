import requests
import json
data = requests.get('https://www.quanmin.tv/json/page/new-ad/info.json')
print(data.text)
data_json = json.dumps(data.json())
print(data_json)

with open('data.json', 'w') as f:
    json.dump(data.json(), f)
