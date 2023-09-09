import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
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
    driver.find_element(by=By.XPATH, value='//input[@id="email"]').send_keys("npraveen0504@gmail.com")
    driver.find_element(by=By.XPATH, value='//input[@id="pass"]').send_keys("Praveen0504!")
    driver.find_element(by=By.XPATH, value='//button[@data-testid="royal_login_button"]').click()

@pytest.mark.usefixtures("setup_browser_firefox")
def test_facebook_registration_page_using_firefox(setup_browser_firefox):

    driver1 = setup_browser_firefox
    driver1.find_element(by=By.XPATH, value='//*[@id="email"]').send_keys("npraveen0504@gmail.com")
    driver1.find_element(by=By.XPATH, value='//*[@id="pass"]').send_keys("Praveen0504!")
    driver1.find_element(by=By.XPATH, value='//*[@data-testid="royal_login_button"]').click()





