from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'https://parsinger.ru/selenium/5.8/2/index.html'

options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument('--headless')


with webdriver.Chrome(options=options_chrome) as driver:
    driver.get(link)
    for button in driver.find_elements(By.CLASS_NAME, 'buttons'):
        button.click()
        alert = driver.switch_to.alert
        code = alert.text
        alert.accept()
        driver.find_element(By.ID, 'input').send_keys(code)
        driver.find_element(By.ID, 'check').click()
        code_received = driver.find_element(By.ID, 'result').text
        if len(code_received.split()) == 1:
            print(code_received)
            exit()
