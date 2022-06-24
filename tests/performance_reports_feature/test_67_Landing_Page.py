import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

url = 'http://localhost:3000/dashboard/homepage'


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


# Test case to open landing page
def test_Landing_Page(browser):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    driver.get(url)
    Landing_page = driver.find_element_by_class_name("home_dashboard__1wZHD")
    assert Landing_page
    driver.quit()


# Test case to interact with dashboard
def test_Interaction_With_Dashboard(browser):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    driver.get(url)
    performance = driver.find_element_by_class_name("home_performanceicon__aCKqk")
    assert performance
    driver.quit()