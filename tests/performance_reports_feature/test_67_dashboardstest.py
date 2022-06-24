import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

url = 'http://localhost:3000/dashboard/performance_page'


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


# Test case to navigate to the performance page
def test_performancepage(browser):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    performance_page = driver.find_element_by_class_name(
        "performance_link__2nUM-")
    assert performance_page
    driver.quit()


# Test case to navigate to a dashboard from the performance page
def test_dashboard(browser):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    driver.get(url)
    driver.find_element_by_class_name("performance_link__2nUM-").click()
    dashboard = driver.find_element_by_xpath('//button[text()="Shop Analytics"]')
    assert dashboard
    driver.quit()
