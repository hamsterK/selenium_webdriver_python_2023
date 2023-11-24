from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

link = 'https://parsinger.ru/selenium/5.8/1/index.html'

options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument('--headless')

with webdriver.Chrome(options=options_chrome) as driver:
    driver.get(link)
    driver.fullscreen_window()
    for button in driver.find_elements(By.CLASS_NAME, 'buttons'):
        button.click()
        driver.switch_to.alert.accept()
        try:
            result = driver.find_element(By.ID, 'result').text
            if result:
                print(result)
                exit()
        except NoSuchElementException:
            continue
