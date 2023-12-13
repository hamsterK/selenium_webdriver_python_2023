import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

with webdriver.Chrome() as driver:
    driver.get('http://parsinger.ru/expectations/1/index.html')
    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'btn'))).click()
    time.sleep(3)
    print(driver.find_element(By.ID, 'result').text)

    # WebDriverWait(browser, poll_frequency=0.5, timeout=10).until(EC.element_to_be_clickable((By.ID, "btn")))
    # poll_frequency - optional, time between attempts
    