import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

url = 'http://localhost:3000/dashboard/dataupload'


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


# Test case to check for file name
def test_filename(browser):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    driver.get(url)
    filename = driver.find_element_by_class_name('card-header').text
    print(filename)
    driver.quit()


# Test case to check for filetype
def test_filetype(browser):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    driver.get(url)
    filetype = driver.find_element_by_class_name('card-header').text
    assert filetype == 'List of Uploaded Files'
    driver.quit()
