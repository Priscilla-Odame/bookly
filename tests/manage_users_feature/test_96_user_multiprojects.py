import pytest
import time
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException 
 
url = 'http://localhost:3000/dashboard/settings/configuration/projectmanagement'
url1 = 'http://localhost:3000/dashboard/settings/configuration/usermanagement'
 
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
 
# Test case for user in multiple projects
def test_for_adding_user_to_multiple_projects(browser):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    driver.get(url)
    driver.find_element_by_class_name("settings_button__2LACs").click()
    driver.implicitly_wait(5)
    driver.find_element_by_class_name("settings_input__WJWPn").send_keys("testcase")
    driver.find_element_by_id("projectDescription").send_keys("test to implement a new project")
    driver.find_element_by_id("addproject").click()
    driver.implicitly_wait(10)
    try:
        WebDriverWait(driver, 3).until(EC.alert_is_present(),
                                   'Timed out waiting for PA creation ' + 
                                   'comfirmation popup to apper.')

        alert = driver.switch_to.alert
        alert.accept()
        print ("alert accepted")
    except TimeoutException:
        print ("no alert")
    # click the user management tab to switch tab
    driver.get(url1)
    # User added to a project
    driver.find_element_by_id("firstname").send_keys("Kojo")
    driver.find_element_by_id("othernames").send_keys("Nartey")
    driver.find_element_by_id("email").send_keys("benedict.nartey@azubiafrica.org")
    driver.find_element_by_id("role").send_keys("admin")
    driver.find_element_by_id("submitbtn").click()
    driver.implicitly_wait(10)
    try:
        WebDriverWait(driver, 3).until(EC.alert_is_present(),
                                   'Timed out waiting for PA creation ' + 
                                   'comfirmation popup to apper.')

        alert = driver.switch_to.alert
        alert.accept()
        print ("alert accepted")
    except TimeoutException:
        print ("no alert")
    driver.refresh()
    # User added to a second project
    driver.find_element_by_id("firstname").send_keys("Kojo")
    driver.find_element_by_id("othernames").send_keys("Nartey")
    driver.find_element_by_id("email").send_keys("benedict.nartey@azubiafrica.org")
    driver.find_element_by_id("role").send_keys("member")
    driver.find_element_by_id("submitbtn").click()
    driver.implicitly_wait(10)
    try:
        WebDriverWait(driver, 3).until(EC.alert_is_present(),
                                   'Timed out waiting for PA creation ' + 
                                   'comfirmation popup to apper.')

        alert = driver.switch_to.alert
        alert.accept()
        print ("alert accepted")
    except TimeoutException:
        print ("no alert")
    driver.refresh()
    # User added to a third project
    driver.find_element_by_id("firstname").send_keys("Kojo")
    driver.find_element_by_id("othernames").send_keys("Nartey")
    driver.find_element_by_id("email").send_keys("benedict.nartey@azubiafrica.org")
    driver.find_element_by_id("role").send_keys("member")
    driver.find_element_by_id("submitbtn").click()
    driver.implicitly_wait(10)
    try:
        WebDriverWait(driver, 3).until(EC.alert_is_present(),
                                   'Timed out waiting for PA creation ' + 
                                   'comfirmation popup to apper.')

        alert = driver.switch_to.alert
        alert.accept()
        print ("alert accepted")
    except TimeoutException:
        print ("no alert")
    driver.quit()