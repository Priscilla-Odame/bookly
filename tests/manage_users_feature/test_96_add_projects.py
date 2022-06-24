import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

url = 'http://localhost:3000/dashboard/settings'


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

# Test case to add project

def test_add_project(browser):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    driver.get(url)
    driver.find_element_by_class_name('settings_projects__3B8q-').click()
    driver.find_element_by_class_name('settings_button__2LACs').click()
    driver.find_element_by_id('projectName').send_keys('solo project')
    driver.find_element_by_id('projectDescription').send_keys('this is a test sample')
    driver.find_element_by_id('addproject').click()
    driver.implicitly_wait(10)
    users_names = driver.find_elements_by_class_name('settings_projectTable__2vIIG')
    print([i.text for i in users_names if i.text == "solo project"])
    driver.quit()
