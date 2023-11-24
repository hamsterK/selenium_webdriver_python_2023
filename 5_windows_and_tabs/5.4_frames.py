"""
switch to iframe:

1. with webelement
iframe = driver.find_element(By.CSS_SELECTOR, "#modal > iframe")
driver.switch_to.frame(iframe)
driver.find_element(By.TAG_NAME, 'button').click()

2. with name or id
driver.switch_to.frame('buttonframe')
driver.find_element(By.TAG_NAME, 'button').click()

3. with index
driver.switch_to.frame(1)

exit frame:
driver.switch_to.default_content()  #obligatory
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:

    driver.get('https://parsinger.ru/selenium/5.8/4/index.html')
    iframe_element = driver.find_element(By.TAG_NAME, 'iframe')
    driver.switch_to.frame(iframe_element)
    iframe_content = driver.page_source
    print(iframe_content)
    