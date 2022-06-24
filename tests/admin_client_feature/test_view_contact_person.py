import pytest
import time
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException 

url = 'http://localhost:3000/dashboard/adminpanel'

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

# Test to view contact person

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
    driver.find_element_by_class_name("dropdown").click
    driver.find_element_by_class_name("dropdown-item").click
    driver.quit
