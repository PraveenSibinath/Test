import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture()
def setup_browser():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.facebook.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture()
def setup_browser_firefox():
    driver1 = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver1.get("https://www.facebook.com/")
    driver1.maximize_window()
    driver1.implicitly_wait(10)
    yield driver1
    driver1.quit()

@pytest.mark.usefixtures("setup_browser")
def test_facebook_registration_page_using_chrome(setup_browser):
    driver = setup_browser
    driver.find_element(by=By.XPATH, value='//*[@class="_42ft _4jy0 _6lti _4jy6 _4jy2 selected _51sy"]').click()
    time.sleep(4)
    driver.find_element(by=By.NAME, value="firstname").send_keys("Praveen")
    driver.find_element(by=By.XPATH, value='//*[@name="lastname"]').send_keys("Sibinath")
    driver.find_element(by=By.XPATH, value='//*[@name="reg_email__"]').send_keys("7544747475")
    driver.find_element(by=By.XPATH, value='//*[@id="password_step_input"]').send_keys("Praveen0504!")
    Select(driver.find_element(by=By.XPATH, value='//*[@name="birthday_day"]')).select_by_value("5")
    Select(driver.find_element(by=By.XPATH, value='//*[@name="birthday_month"]')).select_by_index('3')
    Select(driver.find_element(by=By.XPATH, value='//*[@name="birthday_year"]')).select_by_visible_text('1994')
    driver.find_element(by=By.XPATH, value='//input[@value="2"]').click()
    driver.find_element(by=By.XPATH, value='//*[@name="websubmit"]').click

@pytest.mark.usefixtures("setup_browser_firefox")
def test_facebook_registration_page_using_firefox(setup_browser_firefox):

    driver1 = setup_browser_firefox
    driver1.find_element(by=By.XPATH, value='//*[@class="_42ft _4jy0 _6lti _4jy6 _4jy2 selected _51sy"]').click()
    time.sleep(4)
    driver1.find_element(by=By.NAME, value="firstname").send_keys("Praveen")
    driver1.find_element(by=By.XPATH, value='//*[@name="lastname"]').send_keys("Sibinath")
    driver1.find_element(by=By.XPATH, value='//*[@name="reg_email__"]').send_keys("7544747475")
    driver1.find_element(by=By.XPATH, value='//*[@id="password_step_input"]').send_keys("Praveen0504!")
    Select(driver1.find_element(by=By.XPATH, value='//*[@name="birthday_day"]')).select_by_value("5")
    Select(driver1.find_element(by=By.XPATH, value='//*[@name="birthday_month"]')).select_by_index('3')
    Select(driver1.find_element(by=By.XPATH, value='//*[@name="birthday_year"]')).select_by_visible_text('1994')
    driver1.find_element(by=By.XPATH, value='//input[@value="2"]').click()
    driver1.find_element(by=By.XPATH, value='//*[@name="websubmit"]').click




