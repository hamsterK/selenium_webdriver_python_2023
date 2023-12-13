from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = 'https://parsinger.ru/selenium/5.9/2/index.html'

with webdriver.Chrome() as driver:
    driver.get(link)
    WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.ID, 'qQm9y1rk'))).click()
    print(driver.switch_to.alert.text)
