from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = 'http://parsinger.ru/expectations/3/index.html'

with webdriver.Chrome() as driver:
    driver.get(link)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'btn'))).click()
    WebDriverWait(driver, 60).until(EC.title_is('345FDG3245SFD'))
    print(driver.find_element(By.ID, 'result').text)
