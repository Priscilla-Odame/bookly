import pytest
from selenium.webdriver import Chrome
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.color import Color
url = 'http://localhost:3000/dashboard/engagement/dataupload'


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


# Test case to access upload feature

def test_uploadfeature(browser):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    driver.get(url)
    upload_feature = driver.find_element_by_id("dataupload")
    assert upload_feature
    driver.quit()


# Test case for file upload

def test_uploadfile(browser):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    driver.get(url)
    # choosefilebtn = driver.find_element_by_id("dataupload")
    # choosefilebtn.send_keys(
    #     "/mnt/c/Users/23327/Documents/EventRegistration System.pdf")
    # driver.find_element_by_id("upload").click()


# Multiple file upload

# def test_uploadmultiple(browser):
#     chrome_options = Options()
#     chrome_options.add_argument("--headless")
#     chrome_options.add_argument("--no-sandbox")
#     chrome_options.add_argument('--disable-dev-shm-usage')
#     driver = Chrome(options=chrome_options)
#     driver.implicitly_wait(10)
#     driver.get(url)
#     choosefilebtn = driver.find_element_by_id("dataupload")
#     choosefilebtn.send_keys(
#         "/mnt/c/Users/23327/Documents/EventRegistration System.pdf")
#     choosefilebtn.send_keys(
#         "/mnt/c/Users/23327/Documents/commonAndroidview.pdf")
#     driver.find_element_by_id("upload").click()
