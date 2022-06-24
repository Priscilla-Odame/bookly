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

# Test case to delete global client admin

def test_delete_global_client_administrator(browser):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    driver.get(url)
    driver.find_element_by_class_name("clientorganizationlist_dropdownMenu__1fZrf dropdown").click()
    driver.find_element_by_class_name("dropdown-item").click()
    driver.find_element_by_id("dropdownMenuButton").click()
    driver.find_element_by_class_name("dropdown-item").click()
    deletebtn = find_element_by_class_name("prompt_btn__3sapK")
    deletebtn.click()
    driver.quit()