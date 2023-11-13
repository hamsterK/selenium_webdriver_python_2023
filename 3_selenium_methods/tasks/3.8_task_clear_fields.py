import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'https://parsinger.ru/selenium/5.5/2/1.html'

with webdriver.Chrome() as driver:
    driver.get(link)
    for field in driver.find_elements(By.XPATH, '//input[@type="text"]'):
        if field.is_enabled():
            field.clear()
    driver.find_element(By.ID, 'checkButton').click()
    print(driver.switch_to.alert.text)
