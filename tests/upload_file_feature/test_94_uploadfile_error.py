import pytest
from selenium.webdriver import Chrome
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.color import Color


url = 'https://the-internet.herokuapp.com/upload'
filepath = "mnt/c/Users/GIBT-3/Pictures/Screenshots"



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



# Test case for file upload error message.
def test_for_upload_error_message(browser):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    driver.get(url)
    WebEleme = driver.find_element_by_id("file-upload")
    WebEleme.send_keys(filepath)
    driver.find_element_by_id("upload").click()
    # driver.find_element_by_id("dataupload-files")
    # assert upload_feature
    driver.quit()