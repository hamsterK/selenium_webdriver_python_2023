from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'https://parsinger.ru/selenium/5.5/1/1.html'

with webdriver.Chrome() as driver:
    driver.get(link)
    for element in driver.find_elements(By.XPATH, '//input[@type="text"]'):
        element.clear()
    driver.find_element(By.TAG_NAME, 'button').click()
    print(driver.switch_to.alert.text)
