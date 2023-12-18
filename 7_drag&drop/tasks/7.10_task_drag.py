import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument('--start-maximized')
options_chrome.add_argument('--force-device-scale-factor=1')

with webdriver.Chrome(options=options_chrome) as driver:
    driver.get("https://parsinger.ru/selenium/5.10/8/index.html")
    start = driver.find_elements(By.CSS_SELECTOR, "#pieces_container > div")
    end = driver.find_elements(By.CSS_SELECTOR, "#main_container > div")
    actions = ActionChains(driver)
    for start_point, end_point in zip(start, end):
        actions.drag_and_drop(start_point, end_point).perform()
    print(driver.find_element(By.ID, 'message').text)
