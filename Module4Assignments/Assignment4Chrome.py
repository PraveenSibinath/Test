from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.facebook.com/")
total=driver.find_elements(By.TAG_NAME,"a")
print(len(total))
print("Following are the link present in the webpage")
for totals in total:
    print(totals.text)
