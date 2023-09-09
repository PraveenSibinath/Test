import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.facebook.com/")
driver.find_element(by=By.XPATH, value='//*[@class="_42ft _4jy0 _6lti _4jy6 _4jy2 selected _51sy"]').click()
time.sleep(4)
firstname1 = driver.find_element(by=By.NAME, value="firstname")
firstname1.send_keys("Praveen")
firstname1.clear()
firstname2 = driver.find_element(by=By.NAME, value="firstname")
firstname2.send_keys("Praveen")
print(firstname2.get_attribute("value"))
driver.close()
