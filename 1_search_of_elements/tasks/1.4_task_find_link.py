from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'http://parsinger.ru/selenium/2/2.html'
with webdriver.Chrome() as driver:
    driver.get(url)
    link = driver.find_element(By.LINK_TEXT, '16243162441624')
    link.click()
    print(driver.find_element(By.ID, 'result').text)
