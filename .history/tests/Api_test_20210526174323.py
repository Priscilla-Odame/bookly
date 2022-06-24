import requests
import json
import jsonpath

def testapi ():
    host_url = "https://pia.northeurope.cloudapp.azure.com/api/tickets.json"

    f = open('/home/eli/ProjectFolder/Push%20Insights/tests/request.json','r')
    request_json = json.loads(f.read())
    response = (host_url,request_json)
    print(response.te)
    
    # response_code = requests.post(host_url+"name",data= body)
    # print (response_code)

# response_result = (json.dumps(response_code.json(),indent=4))

# print (response_result)