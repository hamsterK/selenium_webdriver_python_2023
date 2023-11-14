from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'https://parsinger.ru/selenium/5.5/3/1.html'

with webdriver.Chrome() as driver:
    answer = 0
    driver.get(link)
    for element in driver.find_elements(By.CLASS_NAME, 'parent'):
        if element.find_element(By.CLASS_NAME, 'checkbox').is_selected():
            answer += int(element.find_element(By.CSS_SELECTOR, 'textarea').text)
    print(answer)
