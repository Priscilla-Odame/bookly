from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication
import pprint
from azure.devops.credentials import BasicAuthentication
from azure.devops.connection import Connection
from os import read
import requests
import json
import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import pathlib

personal_access_token = 'komm7y5wzb4sbmhdamtqxnmpbuhqs6alqjunjpub4mjdta6ssfqq'
organization_url = 'https://dev.azure.com/Scaleworks'

credentials = BasicAuthentication('', personal_access_token)
connection = Connection(base_url=organization_url, creds=credentials)

url ='https://pushinsights-fe.azurewebsites.net/auth/login'

current_dir = pathlib.Path(__file__).parent.resolve()
# print(f"{current_dir}/files/commonAndroidview.pdf")



@pytest.fixture
def browser():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    driver = Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture 
def function_record(record_property):
    record_property("blahh", "blah")
    assert True

# Function for custom parameters to xml file
@pytest.fixture  
def function(record_xml_attribute):
        record_xml_attribute("owner", "Mr.Danku")
        record_xml_attribute("path", f"{current_dir}/test-results.xml")
        record_xml_attribute("href", f"{current_dir}/test-results.xml")
        # record_xml_attribute("failure.InnerText", "Not an Error")
        # record_xml_attribute("InnerText", "Not an Error")
        # record_xml_attribute("system-out", "Error")
        # record_xml_attribute("system-out", "Acceptance Criteria blah blah")
        

        # std output to print as attachment on AzureBoard
        link_to_work_item = ("https://dev.azure.com/Scaleworks/Push%20Insights/"
                             "_backlogs/backlog/Push%20Insights%20Team/Backlog%20items/?workitem=882")
        
        #Acceptance Criteria 
        Acceptance_criteria_1 = ("User should be able to select files to upload")
        Acceptance_criteria_2 = ("User should be able to view the files that he has selected for upload")
        Acceptance_criteria_3 = ("User should be able to see all the files that have been uploaded")
        Acceptance_criteria_4 = ("User should be able to delete any of the uploaded files")
        Acceptance_criteria_5 = ("User should be able to remove a file from the list of files selected for upload")

        print(f"link to work item : {link_to_work_item}\n"
        f"Acceptance Criteria 1: {Acceptance_criteria_1}\n"
        f"Acceptance Criteria 2: {Acceptance_criteria_2}\n"
        f"Acceptance Criteria 3: {Acceptance_criteria_3}\n"
        f"Acceptance Criteria 4: {Acceptance_criteria_4})\n"
        f"Acceptance Criteria 4: {Acceptance_criteria_5}")
        assert True



# Test Case - user to select file/s to upload and is able to view file selected.

def test_upload_file(browser,function,function_record):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    driver.get(url)
    driver.find_element_by_id("signup-email").send_keys("Misty@awesome.aws")
    driver.find_element_by_id("signup-password").send_keys("awesome")
    button = driver.find_element_by_class_name("passwordreset_btn__3dWlD")
    button.click()
    driver.implicitly_wait(60)
    path1 = "/files/commonAndroidview.pdf"
    path2 = "/files/testfilepush.txt"
    selectfilebtn = driver.find_element_by_id("select-file-in")
    wait = WebDriverWait(driver, 30)
    selectfilebtn = wait.until(EC.presence_of_element_located((By.ID, 'select-file-in')))
    selectfilebtn.send_keys(f"{current_dir}"+ path1)
    wait = WebDriverWait(driver, 30)
    selectfilebtn = wait.until(EC.presence_of_element_located((By.ID, 'select-file-in')))
    selectfilebtn.send_keys(f"{current_dir}"+ path2)
    
    names = driver.find_elements_by_id("file-instance") 
    expected_value_1 = "commonAndroidview.pdf"
    expected_value_2 = "testfilepush.txt"
    found = False
    for name in names:
        if name.text == expected_value_1 or name.text == expected_value_2:
            found = True
        assert found

    driver.quit()


# Test Case - user to be able to remove file from selected list.

def test_remove_file(browser,function,function_record):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    driver.get(url)
    driver.find_element_by_id("signup-email").send_keys("Misty@awesome.aws")
    driver.find_element_by_id("signup-password").send_keys("awesome")
    button = driver.find_element_by_class_name("passwordreset_btn__3dWlD")
    button.click()
    driver.implicitly_wait(60)
    path1 = "/files/commonAndroidview.pdf"
    selectfilebtn = driver.find_element_by_id("select-file-in")
    wait = WebDriverWait(driver, 30)
    selectfilebtn = wait.until(EC.presence_of_element_located((By.ID, 'select-file-in')))
    selectfilebtn.send_keys(f"{current_dir}"+ path1)
    wait = WebDriverWait(driver, 30)
    closebtn = driver.find_element_by_class_name("modal-close")
    
    
    names = driver.find_elements_by_id("file-instance")
    expected_value_1 = "commonAndroidview.pdf"
    found = False
    for name in names:
        if name.text == expected_value_1:
            closebtn.click()
            break
    wait = WebDriverWait(driver, 10)
    
    no_file = driver.find_element_by_id("no-file-selected")
    if no_file:
        found = True
    assert found

    driver.quit()




# Test case to access whether user can upload file and view file uploaded

def test_uploadfeature(browser,function,function_record):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    driver.get(url)
    driver.find_element_by_id("signup-email").send_keys("Misty@awesome.aws")
    driver.find_element_by_id("signup-password").send_keys("awesome")
    button = driver.find_element_by_class_name("passwordreset_btn__3dWlD")
    button.click()
    driver.implicitly_wait(60)
    selectfilebtn = driver.find_element_by_id("select-file-in")
    wait = WebDriverWait(driver, 30)
    selectfilebtn = wait.until(EC.presence_of_element_located((By.ID, 'select-file-in')))
    selectfilebtn.send_keys(f"{current_dir}/files/testfilepush.txt")
    driver.find_element_by_class_name("upload_btn_upload__3WhPH").click()
    driver.implicitly_wait(60)
    file_names = driver.find_elements_by_class_name("td-file-name")
    found = False
    for name in file_names:
        if name.text == "testfilepush.txt":
            found = True
            break
    assert found
    driver.quit()




# Test Case to delete a file uploaded from the list
# def test_delete(browser, function,function_record):
#     chrome_options = Options()
#     chrome_options.add_argument("--headless")
#     chrome_options.add_argument("--no-sandbox")
#     chrome_options.add_argument('--disable-dev-shm-usage')
#     driver = Chrome(options=chrome_options)
#     driver.implicitly_wait(10)
#     driver.get(url)
#     driver.find_element_by_id("signup-email").send_keys("Misty@awesome.aws")
#     driver.find_element_by_id("signup-password").send_keys("awesome")
#     button = driver.find_element_by_class_name("passwordreset_btn__3dWlD")
#     button.click()
    # driver.implicitly_wait(60)
    # wait = WebDriverWait(driver, 30)
    # wait.until(EC.presence_of_element_located((By.ID, 'del-file')))
    # delete = driver.find_element_by_id('del-file')

    # file_names = driver.find_elements_by_class_name("td-file-name")
    # found = False
    # for name in file_names:
    #     if name.text == "testfilepush.txt":
    #         delete.click()
    #         found = True
    #         break
    # assert found
    # driver.quit()          



#Update the Api to send comment after run
# def test_updateapi ():
#     headers = {"content-type": "application/json",
#                    "username": "Elikem.Danku@azubiafrica.org",
#                    "personal_access_token":'komm7y5wzb4sbmhdamtqxnmpbuhqs6alqjunjpub4mjdta6ssfqq' ,
#                    }

#     host_url = "https://dev.azure.com/Scaleworks/Push%20Insights/_apis/test/Runs/6/results?api-version=6.0"


#     f = open(f"{current_dir}/files/request.json",'r+')
#     request_json = json.load(f)
#     print(request_json)
#     response = requests.patch(url=host_url, json=request_json, headers=headers)
#     print(response.text)
#     print (response)



# test_updateapi()