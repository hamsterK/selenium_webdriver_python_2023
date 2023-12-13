from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = 'https://parsinger.ru/selenium/5.9/4/index.html'

with webdriver.Chrome() as driver:
    driver.fullscreen_window()
    driver.get(link)
    driver.execute_script("document.body.style.zoom = '0.75'")
    close_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'close')))
    driver.execute_script("arguments[0].click();", close_button)
    WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.ID, 'ad')))
    button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.TAG_NAME, 'button')))
    driver.execute_script("arguments[0].click();", button)
    print(driver.find_element(By.ID, 'message').text)
