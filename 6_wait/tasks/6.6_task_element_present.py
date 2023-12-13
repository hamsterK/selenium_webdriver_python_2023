from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = 'https://parsinger.ru/expectations/6/index.html'

with webdriver.Chrome() as driver:
    driver.get(link)
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'btn'))).click()
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, 'BMH21YY')))
    print(driver.find_element(By.CLASS_NAME, 'BMH21YY').text)
