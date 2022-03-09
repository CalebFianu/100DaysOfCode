import requests
import json

req = requests.get("https://jsonplaceholder.typicode.com / todos")
varr = json.loads(req.text)
print(varr)