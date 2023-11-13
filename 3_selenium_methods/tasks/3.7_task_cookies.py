from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'https://parsinger.ru/methods/3/index.html'

with webdriver.Chrome() as driver:
    driver.get(link)
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.ID, 'result')))
    cookies = driver.get_cookies()
    print(sum(int(cookie['value']) if int(cookie['name'][-1]) % 2 == 0 else 0 for cookie in cookies))
