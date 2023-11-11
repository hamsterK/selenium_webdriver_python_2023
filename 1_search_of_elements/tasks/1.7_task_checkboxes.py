from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'http://parsinger.ru/selenium/4/4.html'
with webdriver.Chrome() as driver:
    driver.get(url)
    for element in driver.find_elements(By.CLASS_NAME, 'check'):
        element.click()
    driver.find_element(By.CLASS_NAME, 'btn').click()
    print(driver.find_element(By.ID, 'result').text)
