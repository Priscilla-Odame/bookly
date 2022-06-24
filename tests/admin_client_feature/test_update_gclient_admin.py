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

# Test case to update global client administrator

def test_update_global_client_administrator(browser):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    driver.get(url)
    driver.find_element_by_name("dropdown").click()
    driver.find_element_by_class_name("dropdown-item").click()
    name = driver.find_element_by_name("text").sendkeys("James Tagor")
    number = driver.find_element_by_class_name("bootstrapmodal_input__39QQh").sendkeys("+233200445513")
    submitbtn = find_element_by_class_name("bootstrapmodal_btn2__1qof2 text-light float-right")
    submitbtn.click()
    assert name
    assert = number
    driver.quit()