from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://parsinger.ru/scroll/4/index.html'

with webdriver.Chrome() as driver:
    driver.get(link)
    answer = 0
    elements = driver.find_elements(By.CLASS_NAME, 'btn')
    for element in elements:
        driver.execute_script("return arguments[0].scrollIntoView(true);", element)
        element.click()
        answer += int(driver.find_element(By.ID, 'result').text)
    print(answer)