import pytest
from selenium.webdriver import Chrome
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.color import Color
url = 'http://localhost:3000/signup'


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

# Testcase for empty email field


def test_rejectemptyemail(browser):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    driver.get(url)
    driver.find_element_by_id("email").send_keys("")
    driver.find_element_by_id("firstname").send_keys("Elikem")
    driver.find_element_by_id("position").send_keys("Manager")
    driver.find_element_by_id("password").send_keys("Testcase12#")
    driver.find_element_by_id("lastname").send_keys("Manager")
    driver.find_element_by_id("company").send_keys("GetInnotized")
    driver.find_element_by_id("phonenumber").send_keys("0274428578")
    submitbtn = driver.find_element_by_css_selector(".signup_button__1Ls8X").click()
    driver.implicitly_wait(10)
    color = driver.find_element_by_class_name("signup_errorInput__3ZwAG").value_of_css_property("border-top-color")
    hex = Color.from_string(color).hex
    print("color is " + color)
    assert hex == "#df265e"
    driver.quit()

# Test case for empty firstname


# def test_rejectemptyfirstname(browser):
#     chrome_options = Options()
#     chrome_options.add_argument("--headless")
#     chrome_options.add_argument("--no-sandbox")
#     chrome_options.add_argument('--disable-dev-shm-usage')
#     driver = Chrome(options=chrome_options)
#     driver.implicitly_wait(10)
#     driver.get(url)
#     driver.find_element_by_id("email").send_keys("dankuelikem@gmail.com")
#     driver.find_element_by_name("firstname").send_keys("")
#     driver.find_element_by_id("position").send_keys("Manager")
#     driver.find_element_by_id("password").send_keys("Testcase12#")
#     driver.find_element_by_id("lastname").send_keys("bright")
#     driver.find_element_by_id("company").send_keys("GetInnotized")
#     driver.find_element_by_id("phonenumber").send_keys("0274428578")
#     submitbtn = driver.find_element_by_css_selector(".signup_button__1Ls8X").click()
#     color = driver.find_element_by_class_name("signup_errorInput__3ZwAG").value_of_css_property("border-top-color")
#     hex = Color.from_string(color).hex
#     print("color is " + color)
#     assert hex == "#df265e"
#     driver.quit()


# #  Testcase for empty position

# def test_rejectemptyposition(browser):
#     chrome_options = Options()
#     chrome_options.add_argument("--headless")
#     chrome_options.add_argument("--no-sandbox")
#     chrome_options.add_argument('--disable-dev-shm-usage')
#     driver = Chrome(options=chrome_options)
#     driver.implicitly_wait(10)
#     driver.get(url)
#     driver.find_element_by_id("email").send_keys("dankuelikem@gmail.com")
#     driver.find_element_by_name("firstname").send_keys("Elikem")
#     driver.find_element_by_id("position").send_keys("")
#     driver.find_element_by_id("password").send_keys("Testcase12#")
#     driver.find_element_by_id("lastname").send_keys("bright")
#     driver.find_element_by_id("company").send_keys("GetInnotized")
#     driver.find_element_by_id("phonenumber").send_keys("0274428578")
#     submitbtn = driver.find_element_by_css_selector(".signup_button__1Ls8X").click()
#     color = driver.find_element_by_class_name("signup_errorInput__3ZwAG").value_of_css_property("border-top-color")
#     hex = Color.from_string(color).hex
#     print("color is " + color)
#     assert hex == "#df265e"
#     driver.quit()


# #  Testcase for invalid password

# def test_rejectinvalidpassword(browser):
#     chrome_options = Options()
#     chrome_options.add_argument("--headless")
#     chrome_options.add_argument("--no-sandbox")
#     chrome_options.add_argument('--disable-dev-shm-usage')
#     driver = Chrome(options=chrome_options)
#     driver.implicitly_wait(10)
#     driver.get(url)
#     driver.find_element_by_id("email").send_keys("dankuelikem@gmail.com")
#     driver.find_element_by_name("firstname").send_keys("Elikem")
#     driver.find_element_by_id("position").send_keys("Manager")
#     driver.find_element_by_id("password").send_keys("estcase#")
#     driver.find_element_by_id("lastname").send_keys("bright")
#     driver.find_element_by_id("company").send_keys("GetInnotized")
#     driver.find_element_by_id("phonenumber").send_keys("0274428578")
#     submitbtn = driver.find_element_by_css_selector(".signup_button__1Ls8X").click()
#     color = driver.find_element_by_class_name("signup_errorInput__3ZwAG").value_of_css_property("border-top-color")
#     hex = Color.from_string(color).hex
#     print("color is " + color)
#     assert hex == "#df265e"
#     driver.quit()

# #  Testcase for empty last name


# def test_rejectemptylastname(browser):
#     chrome_options = Options()
#     chrome_options.add_argument("--headless")
#     chrome_options.add_argument("--no-sandbox")
#     chrome_options.add_argument('--disable-dev-shm-usage')
#     driver = Chrome(options=chrome_options)
#     driver.implicitly_wait(10)
#     driver.get(url)
#     driver.find_element_by_id("email").send_keys("dankuelikem@gmail.com")
#     driver.find_element_by_name("firstname").send_keys("Elikem")
#     driver.find_element_by_id("position").send_keys("Manager")
#     driver.find_element_by_id("password").send_keys("Testcase12#")
#     driver.find_element_by_id("lastname").send_keys("")
#     driver.find_element_by_id("company").send_keys("GetInnotized")
#     driver.find_element_by_id("phonenumber").send_keys("0274428578")
#     submitbtn = driver.find_element_by_css_selector(".signup_button__1Ls8X").click()
#     color = driver.find_element_by_class_name("signup_errorInput__3ZwAG").value_of_css_property("border-top-color")
#     hex = Color.from_string(color).hex
#     print("color is " + color)
#     assert hex == "#df265e"
#     driver.quit()

# #  Testcase for empty company


# def test_rejectemptycompany(browser):
#     chrome_options = Options()
#     chrome_options.add_argument("--headless")
#     chrome_options.add_argument("--no-sandbox")
#     chrome_options.add_argument('--disable-dev-shm-usage')
#     driver = Chrome(options=chrome_options)
#     driver.implicitly_wait(10)
#     driver.get(url)
#     driver.find_element_by_id("email").send_keys("dankuelikem@gmail.com")
#     driver.find_element_by_name("firstname").send_keys("Elikem")
#     driver.find_element_by_id("position").send_keys("Manager")
#     driver.find_element_by_id("password").send_keys("Testcase12#")
#     driver.find_element_by_id("lastname").send_keys("Bright")
#     driver.find_element_by_id("company").send_keys("")
#     driver.find_element_by_id("phonenumber").send_keys("0274428578")
#     submitbtn = driver.find_element_by_css_selector(".signup_button__1Ls8X").click()
#     color = driver.find_element_by_class_name("signup_errorInput__3ZwAG").value_of_css_property("border-top-color")
#     hex = Color.from_string(color).hex
#     print("color is " + color)
#     assert hex == "#df265e"
#     driver.quit()

# # Test case for invalid password


# def test_rejectinvalidnumber(browser):
#     chrome_options = Options()
#     chrome_options.add_argument("--headless")
#     chrome_options.add_argument("--no-sandbox")
#     chrome_options.add_argument('--disable-dev-shm-usage')
#     driver = Chrome(options=chrome_options)
#     driver.implicitly_wait(10)
#     driver.get(url)
#     driver.find_element_by_id("email").send_keys("dankuelikem@gmail.com")
#     driver.find_element_by_name("firstname").send_keys("Elikem")
#     driver.find_element_by_id("position").send_keys("Manager")
#     driver.find_element_by_id("password").send_keys("Testcase12#")
#     driver.find_element_by_id("lastname").send_keys("Bright")
#     driver.find_element_by_id("company").send_keys("GetInotized")
#     driver.find_element_by_id("phonenumber").send_keys("0274hfkkks")
#     submitbtn = driver.find_element_by_css_selector(".signup_button__1Ls8X").click()
#     color = driver.find_element_by_class_name("signup_errorInput__3ZwAG").value_of_css_property("border-top-color")
#     hex = Color.from_string(color).hex
#     print("color is " + color)
#     assert hex == "#df265e"
#     driver.quit()
