from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'https://parsinger.ru/selenium/5.5/4/1.html'

with webdriver.Chrome() as driver:
    driver.get(link)
    for element in driver.find_elements(By.CLASS_NAME, 'parent'):
        number = element.find_element(By.CSS_SELECTOR, 'textarea[color="gray"]').text
        element.find_element(By.CSS_SELECTOR, 'textarea[color="gray"]').clear()
        element.find_element(By.CSS_SELECTOR, 'textarea[color="blue"]').send_keys(number)
        element.find_element(By.CSS_SELECTOR, 'button').click()
    driver.find_element(By.ID, 'checkAll').click()
    print(driver.find_element(By.ID, 'congrats').text)