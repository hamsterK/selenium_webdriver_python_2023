import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'https://parsinger.ru/selenium/5.9/5/index.html'

with webdriver.Chrome() as driver:
    driver.get(link)
    answer = []
    for element in driver.find_elements(By.CLASS_NAME, 'box_button'):
        element.click()
        driver.find_element(By.ID, 'close_ad').click()
        while len(element.text) == 0:
            time.sleep(1)
        answer.append(element.text)
    print('-'.join(answer))
