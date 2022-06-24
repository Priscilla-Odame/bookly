import pytest
import time
from os import read
import requests
import json
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pathlib


url ='https://pushinsights-fe.azurewebsites.net/auth/login'
current_dir = pathlib.Path(__file__).parent.resolve()


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

         # std output to print as attachment on AzureBoard
        link_to_work_item = ("https://dev.azure.com/Scaleworks/Push%20Insights/"
                             "_backlogs/backlog/Push%20Insights%20Team/Backlog%20items/?workitem=882")
        
        #Acceptance Criteria 
        Acceptance_criteria_1 = ("User should be able to view the upload progress for each of the files he is uploading")
        Acceptance_criteria_2 = ("User should be able to to view the final upload status for each of the the files he uploaded")
        Acceptance_criteria_3 = ("User should be able to filter through the files by date uploaded")
        Acceptance_criteria_4 = ("User should be able to filter through the files by name of the file")
        Acceptance_criteria_5 = ("Files listing pane should be paginated if more than 20 files are uploaded.")

        print(f"link to work item : {link_to_work_item}\n"
        f"Acceptance Criteria 1: {Acceptance_criteria_1}\n"
        f"Acceptance Criteria 2: {Acceptance_criteria_2}\n"
        f"Acceptance Criteria 3: {Acceptance_criteria_3}\n"
        f"Acceptance Criteria 4: {Acceptance_criteria_4})\n"
        f"Acceptance Criteria 5: {Acceptance_criteria_5}")
        assert True



# Test case for user to search for uploaded files
def test_search_file(browser,function,function_record):
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
    search = driver.find_element_by_class_name("uploads_search_input__2ksP6")
    search.send_keys("inno")
    search.send_keys(Keys.ENTER)
    driver.implicitly_wait(30)
    try:
        search_result = WebDriverWait(driver, 10).until(
	        EC.presence_of_element_located((By.CLASS_NAME, "uploads_searchResults__vgADx"))
        )
    
        files = search_result.find_elements_by_tag_name("a")
        for file in files:
	        filename = file.find_element_by_tag_name("p")
	        filename.text
	        assert filename.text == "inno2.png"

    finally:
         driver.quit()



# Test Case to view the upload progress for each of the files he is uploading 

def test_uploadfeature(browser, function, function_record):
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

    progress_bar = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'progress-bar')))
    available = False
    if progress_bar:
        available = True
    assert available
    driver.quit()