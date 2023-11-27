import math
from selenium import webdriver
from selenium.webdriver.common.by import By

sites = ['http://parsinger.ru/blank/1/1.html', 'http://parsinger.ru/blank/1/2.html', 'http://parsinger.ru/blank/1/3.html',
         'http://parsinger.ru/blank/1/4.html', 'http://parsinger.ru/blank/1/5.html', 'http://parsinger.ru/blank/1/6.html',]

answer = 0.0
for site in sites:
    with webdriver.Chrome() as driver:
        driver.get(site)
        driver.find_element(By.CLASS_NAME, 'checkbox_class').click()
        result = int(driver.find_element(By.ID, 'result').text)
        answer += math.sqrt(result)

print(round(answer, 9))
