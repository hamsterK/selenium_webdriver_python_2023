import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'https://parsinger.ru/selenium/5.9/7/index.html'

with webdriver.Chrome() as driver:
    driver.get(link)
    for container in driver.find_elements(By.CLASS_NAME, 'container'):
        while container.get_attribute('style') != 'background-color: green;':
            container.find_element(By.CSS_SELECTOR, 'button').click()
    print(driver.find_element(By.ID, 'result').text)
