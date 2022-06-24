from os import read
import requests
import json

def testapi ():
    headers = {"content-type": "application/json",
                   "X-API-Key": "22E57D39163D52CC1CE53F2CDA306049"}

    host_url = "https://pia.northeurope.cloudapp.azure.com/api/tickets.json"

    f = open('/home/eli/ProjectFolder/Push%20Insights/tests/api_test/request.json','r+')
    request_json = json.load(f)
    print(request_json)
    response = requests.post(url=host_url, json=request_json,headers=headers)
    print(response.text)
    print (response)

# If you want to run with python command
testapi()
#Bright Elikem