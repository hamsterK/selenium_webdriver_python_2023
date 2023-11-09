from selenium import webdriver
from selenium.webdriver.common.by import By


url = 'http://parsinger.ru/selenium/3/3.html'
with webdriver.Chrome() as driver:
    driver.get(url)
    elements = driver.find_elements(By.TAG_NAME, 'p')
    print(sum([int(i.text) for i in elements]))
