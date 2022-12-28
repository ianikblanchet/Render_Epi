import requests
import json

base = "http://127.0.0.1:8000/"

list = json.dumps({'token' : 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImlhbmlrLmJsYW5jaGV0QGdtYWlsLmNvbSIsImV4cCI6MTY3MjI3Mzc0Ni4wNzIzMDgzfQ.dgaITs2bhAKXJBVIWEsYL1PYLF1rpFCPr5xP6EVJphM'})


print(type(list))

response = requests.post(base + "decode" , data = list)

print (response.json())