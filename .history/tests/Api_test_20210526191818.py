from os import read
import requests
import json

def testapi ():
    host_url = "https://pia.northeurope.cloudapp.azure.com/api/tickets.json"

    with open('data.json') as json_file:
        data = json.load(json_file)

    # f = open('/home/eli/ProjectFolder/Push%20Insights/tests/request.json','r')
    # readme = f.read()
    # # f.close()
    # # request_json = json.loads(readme)
    # request_json = json.load(f)
    response = requests.get(url=host_url, json=)
    print(response.text)
    
    # response_code = requests.post(host_url+"name",data= body)
    # print (response_code)

# response_result = (json.dumps(response_code.json(),indent=4))

# print (response_result)