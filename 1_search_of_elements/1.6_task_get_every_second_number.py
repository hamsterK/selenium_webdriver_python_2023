from selenium import webdriver
from selenium.webdriver.common.by import By


url = 'http://parsinger.ru/selenium/3/3.html'
with webdriver.Chrome() as driver:
    driver.get(url)
    elements = driver.find_elements(By.XPATH, '//div[@class="text"]/p[2]')
    print(sum([int(i.text) for i in elements]))
