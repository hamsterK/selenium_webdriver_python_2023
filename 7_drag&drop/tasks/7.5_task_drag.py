import time
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/draganddrop/3/index.html')
    time.sleep(1)
    block1 = browser.find_element(By.ID, 'block1')
    actions = ActionChains(browser)
    actions.click_and_hold(block1)
    for x in range(6):
        actions.move_by_offset(50, 0)
    actions.perform()
    print(WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, 'message'))).text)
