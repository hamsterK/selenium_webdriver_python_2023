from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

link = 'https://parsinger.ru/draganddrop/1/index.html'

with webdriver.Chrome() as driver:
    driver.get(link)
    drag_start = driver.find_element(By.ID, 'draggable')
    drag_end = driver.find_element(By.ID, 'field2')
    ActionChains(driver).drag_and_drop(drag_start, drag_end).perform()
    print(driver.find_element(By.ID, 'result').text)
