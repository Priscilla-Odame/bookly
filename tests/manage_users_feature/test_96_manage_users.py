import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select 
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.color import Color
url = 'http://localhost:3000/dashboard/settings'
url1 = 'http://localhost:3000/dashboard/settings/configuration/usermanagement'


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


# Test case to manage users

def test_uploadfeature(browser):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    driver.get(url)
    driver.get(url1)
    driver.find_element_by_id("firstname").send_keys("Elikem")
    driver.find_element_by_id("othernames").send_keys("Bright")
    driver.find_element_by_id("email").send_keys("dankuelikem@gmail.com")
    select= Select(driver.find_element_by_id("role"))
    select.select_by_value("admin ")
    driver.find_element_by_id("submitbtn").click()
    driver.implicitly_wait(10)
    obj = driver.switch_to.alert.dismiss()
    # obj.accept()
    driver.find_element_by_class_name("settings_MemberList__28Cy1")
    driver.find_elements_by_class_name("settings_Addbutton__1roDy").click()