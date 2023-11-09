from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://parsinger.ru/selenium/6/6.html'

with webdriver.Chrome() as driver:
    driver.get(link)
    calculation = eval(driver.find_element(By.ID, 'text_box').text)
    # driver.find_element(By.XPATH, "//select[@id='selectId']").click()
    driver.find_element(By.XPATH, f"//option[text()={calculation}]").click()
    driver.find_element(By.ID, 'sendbutton').click()
    print(driver.find_element(By.ID, 'result').text)
