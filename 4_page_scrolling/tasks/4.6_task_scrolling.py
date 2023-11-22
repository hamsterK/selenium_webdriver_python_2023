from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = 'http://parsinger.ru/infiniti_scroll_2/'

with webdriver.Chrome() as driver:
    driver.get(link)
    answer = 0
    time.sleep(5)
    scroll_container = driver.find_element(By.CLASS_NAME, 'scroll-container')
    counter = 0
    while True:
        if counter == 100:
            break
        text_field = f'//*[contains(@id, "index_{counter}")]'
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, text_field)))
        answer += int(driver.find_element(By.XPATH, text_field).text)
        driver.execute_script('arguments[0].scrollBy(0, 100);', scroll_container)
        counter += 1
    print(answer)

