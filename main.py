import requests
from requests.auth import HTTPBasicAuth


def api_request(url, user, passw):
    auth = HTTPBasicAuth(user, passw)
    return requests.get(url, auth=auth)
    
request = api_request("https://app-academy-neu-codechallenge.azurewebsites.net/api/2d/cut", "lantekacademy",
":cPIi<kyF(=5OXc")

for row in request.json():
        print("Name: {}, Manufacturer: {}".format(row['name'], row['manufacturer']))
        
