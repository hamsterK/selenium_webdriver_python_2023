import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoAlertPresentException

link = 'https://parsinger.ru/selenium/5.8/5/index.html'

with webdriver.Chrome() as driver:
    driver.get(link)
    driver.fullscreen_window()
    time.sleep(3)
    ActionChains(driver).key_down(Keys.CONTROL).pause(0.1).key_down(Keys.ADD).perform()  # этот код не выполняется, пришлось зумить вручную

    for iframe in driver.find_elements(By.TAG_NAME, 'iframe'):
        driver.switch_to.frame(iframe)
        driver.find_element(By.TAG_NAME, 'button').click()
        number = driver.find_element(By.ID, 'numberDisplay').text
        driver.switch_to.default_content()
        driver.find_element(By.TAG_NAME, 'input').send_keys(number)
        driver.find_element(By.ID, 'checkBtn').click()
        try:
            print(driver.switch_to.alert.text)
        except NoAlertPresentException:
            driver.find_element(By.TAG_NAME, 'input').clear()
