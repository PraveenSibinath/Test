from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.facebook.com/")
driver.find_element(by=By.XPATH, value='//*[@class="_42ft _4jy0 _6lti _4jy6 _4jy2 selected _51sy"]').click()
driver.find_element(by=By.XPATH, value='//*[@id="nav-link-accountList-nav-line-1"]')
driver.find_element(by=By.XPATH, value='//*[@name="firstname"]').send_keys("Praveen")
driver.find_element(by=By.XPATH, value='//*[@name="lastname"]').send_keys("Sibinath")
driver.find_element(by=By.XPATH, value='//*[@name="reg_email__"]').send_keys("7544747477")
driver.find_element(by=By.XPATH, value='//*[@name="name="reg_passwd__"]').send_keys("Praveen0504!")
Select(driver.find_element(by=By.XPATH, value='//*[@name="birthday_day"]')).select_by_value("5")
Select(driver.find_element(by=By.XPATH, value='//*[@name="birthday_month"]')).select_by_value("Apr")
Select(driver.find_element(by=By.XPATH, value='//*[@name="birthday_year"]')).select_by_value("1994")
driver.find_element(by=By.XPATH, value='//*[@//*[@for="u_d_5_3g"]').click()
