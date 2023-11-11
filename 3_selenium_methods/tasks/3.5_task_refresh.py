import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'https://parsinger.ru/methods/1/index.html'

options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument('--headless')

with webdriver.Chrome(options=options_chrome) as driver:
    driver.get(link)
    number = ''
    while not isinstance(number, int):
        try:
            number = int(driver.find_element(By.ID, 'result').text)
        except ValueError:
            driver.refresh()
    print(number)
