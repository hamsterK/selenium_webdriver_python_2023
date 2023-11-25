from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://parsinger.ru/window_size/1/'

options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument('--headless')

with webdriver.Chrome(options=options_chrome) as driver:
    driver.get(link)
    driver.set_window_size(555, 555)
    print(driver.find_element(By.ID, 'result').text)
