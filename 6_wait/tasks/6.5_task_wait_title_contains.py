from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = 'http://parsinger.ru/expectations/4/index.html'

with webdriver.Chrome() as driver:
    driver.get(link)
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'btn'))).click()
    WebDriverWait(driver, poll_frequency=0.1, timeout=60).until(EC.title_contains('JK8HQ'))
    print(driver.title)
