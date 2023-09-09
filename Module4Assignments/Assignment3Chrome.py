import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def setup_browser():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.facebook.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.mark.usefixtures("setup_browser")
def test_facebook_registration_page_using_chrome(setup_browser):
    driver = setup_browser
    driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[5]/a').click()
    time.sleep(10)
    driver.find_element(by=By.XPATH, value="/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[1]/div[1]/div[1]/div/input").send_keys("Praveen")
    driver.find_element(by=By.XPATH, value='/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[1]/div[1]/div[2]/div/div[1]/input').send_keys("Sibinath")
    driver.find_element(by=By.XPATH, value='/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[2]/div/div[1]/input').send_keys("7544747475")
    driver.find_element(by=By.XPATH, value='/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[4]/div/div[1]/input').send_keys("Praveen0504!")
    Select(driver.find_element(by=By.XPATH, value='/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[5]/div[2]/span/span/select[1]')).select_by_value("5")
    Select(driver.find_element(by=By.XPATH, value='/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[5]/div[2]/span/span/select[2]')).select_by_index('3')
    Select(driver.find_element(by=By.XPATH, value='/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[5]/div[2]/span/span/select[3]')).select_by_visible_text('1994')
    driver.find_element(by=By.XPATH, value='/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[7]/span/span[2]/input').click()
    driver.find_element(by=By.XPATH, value='/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[11]/button').click