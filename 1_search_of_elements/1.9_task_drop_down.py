from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'http://parsinger.ru/selenium/7/7.html'

with webdriver.Chrome() as driver:
    driver.get(url)
    driver.find_element(By.XPATH, "//select[@id='opt']").click()
    elements = driver.find_elements(By.TAG_NAME, 'option')
    field = driver.find_element(By.ID, 'input_result')
    field.send_keys(sum(int(element.text) for element in elements))
    driver.find_element(By.ID, 'sendbutton').click()
    print(driver.find_element(By.ID, 'result').text)
