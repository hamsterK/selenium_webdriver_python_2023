from selenium import webdriver
from selenium.webdriver.common.by import By


url = 'http://parsinger.ru/selenium/1/1.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    elements = browser.find_elements(By.CLASS_NAME, 'form')
    for element in elements:
        element.send_keys('Текст')
    button = browser.find_element(By.ID, 'btn')
    button.click()
    print(browser.find_element(By.ID, 'result').text)

