import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'https://parsinger.ru/selenium/5.8/3/index.html'

options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument('--headless')

with webdriver.Chrome(options=options_chrome) as driver:
    driver.get(link)
    for element in driver.find_elements(By.CLASS_NAME, 'pin'):
        code = element.text
        driver.find_element(By.TAG_NAME, 'input').click()
        driver.switch_to.alert.send_keys(code)
        driver.switch_to.alert.accept()
        result = driver.find_element(By.ID, 'result').text
        if len(result.split()) == 1:
            print(result)
            exit()