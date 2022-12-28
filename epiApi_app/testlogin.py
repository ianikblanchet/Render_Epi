import requests
import json

base = "http://127.0.0.1:8000/"

list = json.dumps({'email' : 'ianik.blanchet@gmail.com', 'password': 'fiction'})


print(type(list))

response = requests.post(base + "login" , data = list)

print (response.json())