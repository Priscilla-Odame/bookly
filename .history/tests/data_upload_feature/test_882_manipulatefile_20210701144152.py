import pytest
from selenium.webdriver import Chrome
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.color import Color
url = 'https://pushinsights-fe.azurewebsites.net/upload'


@pytest.fixture
def browser():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    driver = Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


# Test case to access whether user can manipulate their file

def test_uploadfeature(browser):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    driver.get(url)
    choosefilebtn = driver.find_element_by_id("dataupload")
    choosefilebtn.send_keys(
        "/mnt/c/Users/23327/Documents/EventRegistration System.pdf")
    assert "EventRegistration
    
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