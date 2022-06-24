from os import read
import requests
import json

def testapi ():
    host_url = "https://pia.northeurope.cloudapp.azure.com/api/tickets.json"

    # with open('/home/eli/ProjectFolder/Push%20Insights/tests/request.json') as json_file:
        # data = json.load(json_file)
        # print(data)

    f = open('/home/eli/ProjectFolder/Push%20Insights/tests/request.json','r+')
    # readme = f.read()
    # f.close()
    # request_json = json.loads(readme)

    request_json = {"name":"Bright Elikem","subject":"Just a test case","message":"Just a test case","email":"dankuelikem@gmail.com","ip":"172.17.204.33","api_key":"E15C56270642A56A8A164819DC2E6ABE"}
    
    print(request_json)
    response = requests.post(url=host_url, json=data)
    # print(response.text)

    # response_code = requests.post(host_url+"name",data= body)
    # print (response_code)

# response_result = (json.dumps(response_code.json(),indent=4))

# print (response_result)

testapi()