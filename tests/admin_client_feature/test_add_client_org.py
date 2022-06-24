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
    chrome_options.add_argument("--window-size=1920x1080")
    driver = Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
 
# Test case to add client organisation
def test_for_adding_client_org(browser):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    driver.get(url)
    driver.find_element_by_id("add-client-btn").click()
    driver.find_element_by_id("admin-clt-org-name").send_keys("Solo Org")
    driver.find_element_by_id("admin-clt-org-des").send_keys("Tech")
    choosefilebtn = driver.find_element_by_id("admin-clt-org-logo")
    choosefilebtn.send_keys("/mnt/c/Users/23327/Pictures/Solo.jpg")
    driver.find_element_by_id("admin-sub-org-mod-btn").click()
    driver.implicitly_wait(5)
    # Adding Client Administrator
    driver.find_element_by_id("admin-clt-gadmin-name").send_keys("Solomon")
    driver.find_element_by_id("admin-clt-gadmin-email").send_keys("Solo@gmail.com")
    driver.find_element_by_id("admin-clt-gadmin-phone").send_keys("0552554892")
    driver.find_element_by_id("admin-clt-gadmin-role").send_keys("Lead Engineer")
    driver.find_element_by_id("admin-clt-gadmin-mod-sbtn").click()
    driver.implicitly_wait(5)
    # Adding Contact Person
    driver.find_element_by_id("admin-clt-ctc-name").send_keys("Joe")
    driver.find_element_by_id("admin-clt-ctc-phone").send_keys("0224565852")
    driver.find_element_by_id("admin-clt-ctc--role").send_keys("Lead Engineer")
    driver.find_element_by_id("admin-clt-ctc-sbtn").click()
    driver.implicitly_wait(5)
    driver.save_screenshot("clientorglist.png")
    clientorg = driver.page_source().contains("Solo Org")
    assert clientorg
    driver.quit()
    