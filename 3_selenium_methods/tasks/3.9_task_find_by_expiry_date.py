from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'https://parsinger.ru/methods/5/index.html'

with webdriver.Chrome() as driver:
    expiry, result = 0, int()
    driver.get(link)
    for element in driver.find_elements(By.TAG_NAME, 'a'):
        element.click()
        cookies = driver.get_cookies()
        if cookies[0]['expiry'] > expiry:
            expiry = cookies[0]['expiry']
            result = driver.find_element(By.ID, 'result').text
        driver.back()
    print(result)
