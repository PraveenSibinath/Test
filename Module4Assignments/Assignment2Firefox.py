import time
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture()
def setup_browser():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.get("https://profile.oracle.com/myprofile/account/create-account.jspx")
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.mark.usefixtures("setup_browser")
def test_facebook_registration_page_using_firefox(setup_browser):
    driver = setup_browser
    driver.find_element(by=By.XPATH, value='//*[@name="sView1:r1:0:email"]').send_keys("npraveen0504@gmail.com")
    driver.find_element(by=By.XPATH, value='//*[@name="sView1:r1:0:password"]').send_keys("Test123!")
    driver.find_element(by=By.XPATH, value='//*[@name="sView1:r1:0:retypePassword"]').send_keys("Test123!")
    Select(driver.find_element(by=By.XPATH, value='//*[@name="sView1:r1:0:country"]')).select_by_value("IN")
    driver.find_element(by=By.XPATH, value='//*[@name="sView1:r1:0:firstName"]').send_keys("Praveen")
    driver.find_element(by=By.XPATH, value='//*[@name="sView1:r1:0:lastName"]').send_keys("Sibi")
    driver.find_element(by=By.XPATH, value='//*[@name="sView1:r1:0:jobTitle"]').send_keys("Test Engineer")
    driver.find_element(by=By.XPATH, value='//*[@id="sView1:r1:0:workPhone::content"]').send_keys("7402122548")
    driver.find_element(by=By.XPATH, value='//*[@id="sView1:r1:0:companyName::content"]').send_keys("XYZ Company")
    driver.find_element(by=By.XPATH, value='//*[@id="sView1:r1:0:address1::content"]').send_keys("Work Street Corner")
    driver.find_element(by=By.XPATH, value='//*[@id="sView1:r1:0:city::content"]').send_keys("Chennai")
    time.sleep(2)
    Select(driver.find_element(by=By.XPATH, value='//*[@id="sView1:r1:0:state::content"]')).select_by_value("30")
    driver.find_element(by=By.XPATH, value='//*[@id="sView1:r1:0:postalCode::content"]').send_keys("600001")
    driver.find_element(by=By.XPATH, value='//*[@class="xfx"]').click()