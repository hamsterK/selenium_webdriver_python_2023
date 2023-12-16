from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

link = 'https://parsinger.ru/draganddrop/2/index.html'

with webdriver.Chrome() as driver:
    driver.get(link)
    for box in driver.find_elements(By.CLASS_NAME, 'box'):
        ActionChains(driver).drag_and_drop(driver.find_element(By.ID, 'draggable'), box).perform()
    print(driver.find_element(By.ID, 'message').text)
