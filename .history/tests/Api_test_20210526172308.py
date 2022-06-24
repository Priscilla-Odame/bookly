import requests
import json

def testapi ():
    host_url = "https://pia.northeurope.cloudapp.azure.com/api/tickets.json"
    body = "{
        "name":"Benedict Narey",
        "subject" : "",
        "message" :"",
        "email": "",
        "ip" :"",
        "api_key":""
            }​"

    response_code = requests.post(host_url+"name",data=body)
    print (response_code)

# response_result = (json.dumps(response_code.json(),indent=4))

# print (response_result)