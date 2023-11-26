from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://parsinger.ru/blank/3/index.html'

with webdriver.Chrome() as driver:
    driver.get(link)
    answer = 0
    for button in driver.find_elements(By.CLASS_NAME, 'buttons'):
        button.click()
        window_handles = driver.window_handles
        driver.switch_to.window(window_handles[-1])
        answer += int(driver.title)
        driver.switch_to.window(window_handles[0])
    print(answer)
