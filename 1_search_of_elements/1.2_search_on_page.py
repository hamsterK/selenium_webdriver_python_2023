from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'http://parsinger.ru/selenium/3/3.html'
with webdriver.Chrome() as browser:

    # cascade search
    parent_element = browser.find_element(By.ID, 'parent_id')
    child_element = parent_element.find_element(By.CLASS_NAME, 'child_class')
    # OR
    element = browser.find_element(By.ID, 'parent_id').find_element(By.CLASS_NAME, 'child_class')

    # search inside of elements
    blocks = browser.find_elements(By.CLASS_NAME, 'block')
    for block in blocks:
        button = block.find_element(By.CLASS_NAME, 'button')
        button.click()

    # check if elements exist
    elements = browser.find_elements(By.CLASS_NAME, 'some_class')
    if elements:
        elements[0].click()