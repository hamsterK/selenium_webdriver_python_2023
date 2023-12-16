from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

link = "https://parsinger.ru/selenium/5.10/2/index.html"

with webdriver.Chrome() as driver:
    driver.get(link)

    boxes = driver.find_elements(By.CLASS_NAME, 'draganddrop')
    end = driver.find_element(By.CLASS_NAME, 'draganddrop_end')

    actions = ActionChains(driver)
    for box in boxes:
        actions.drag_and_drop(box, end)
    actions.perform()
    print(driver.find_element(By.ID, 'message').text)
