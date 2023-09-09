import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
@pytest.fixture
def driver_initialization():
    driver.get("https://www.amazon.in/")
    driver.maximize_window()
    yield driver
    driver.quit()
