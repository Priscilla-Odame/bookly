import requests
import json

def testapi ():
    host_url = "https://pia.northeurope.cloudapp.azure.com/api/tickets.json"

    f = open('/home/eli/ProjectFolder/Push%20Insights/tests/request.json','r')
    # readme = f.read()
    # f.close()
    request_json = json.loads(f.read())
    response = requests.post(host_url,request_json)
    print(response.text)
    
    # response_code = requests.post(host_url+"name",data= body)
    # print (response_code)

# response_result = (json.dumps(response_code.json(),indent=4))

# print (response_result)