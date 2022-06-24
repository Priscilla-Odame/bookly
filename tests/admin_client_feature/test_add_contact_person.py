import pytest
import time
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException 

url = 'http://pushinsights-fe.azurewebsites.net/dashboard/adminpanel/clientOrganization/b127ead5-0c77-4246-911c-522f5bd8cb85'

@pytest.fixture
def browser():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    # chrome_options.add_argument("--window-size=1920x1080")
    driver = Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

# Test to add contact person

def test_view_contact_person(browser):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    driver.get(url)
    driver.implicitly_wait(10)
    element = driver.find_element_by_xpath("clientorganizationlist_dropdownMenu__1fZrf dropdown-toggle btn btn-primary")
    element.click()
    driver.find_element_by_class_name("dropdown-item").click()
    driver.find_element_by_class_name("ml-3 list_clientBorder__afmb9").click()
    driver.find_element_by_class_name("list_addTxt___csrE").click
    name = driver.find_element_by_class_name("bootstrapmodal_input__39QQh").sendkeys("James Dolly")
    number = driver.find_element_by_class_name("bootstrapmodal_input__39QQh").sendkeys("+233244257945")
    position = driver.find_element_by_class_name("bootstrapmodal_input__39QQh").sendkeys("Lead engineer")
    submit = driver.find_element_by_class_name("bootstrapmodal_input__39QQh")
    submit.click()
    assert name
    assert number
    assert position
    driver.quit
