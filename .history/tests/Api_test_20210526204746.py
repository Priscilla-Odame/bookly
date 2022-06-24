from os import read
import requests
import json

def testapi ():
    headers = {"content-type": "application/json",
                   "X-API-Key": 4AA9D5EFA3F2658C30DDCC1BEB2C7DF6"}
    host_url = "https://pia.northeurope.cloudapp.azure.com/api/tickets.json"
    f = open('/home/eli/ProjectFolder/Push%20Insights/tests/request.json','r+')
    # readme = f.read()
    # f.close()
    request_json = json.load(f)
    
    print(request_json)
    response = requests.post(url=host_url, json=request_json,headers=headers)
    print(response.text)
    print (response)
# response_result = (json.dumps(response_code.json(),indent=4))

# print (response_result)

testapi()