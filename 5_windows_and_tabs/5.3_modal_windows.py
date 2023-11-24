"""
types: alert (ok), prompt (input, ok, cancel), confirm (ok, cancel)

.switch_to
driver.switch_to.alert

.accept  # click OK
driver.switch_to.alert.accept()

.dismiss()  # click Cancel
driver.switch_to.alert.dismiss()

.send_keys()
driver.switch_to.alert.send_keys("Текст для отправки")

.text
driver.switch_to.alert.text
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/blank/modal/1/index.html')
    browser.find_element(By.ID, 'confirm').click()
    time.sleep(2)
    prompt = browser.switch_to.alert
    prompt.accept()  # or dismiss()
    time.sleep(.5)
