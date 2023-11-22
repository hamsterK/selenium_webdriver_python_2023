import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


link = 'https://parsinger.ru/infiniti_scroll_1/'

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
        checkbox = f'//*[contains(@id, "_index_{counter}")]/input'
        input_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, checkbox)))
        input_field.click()
        answer += int(driver.find_element(By.XPATH, text_field).text)
        driver.execute_script('arguments[0].scrollBy(0, 100);', scroll_container)
        counter += 1
    print(answer)
