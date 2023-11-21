from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

link = 'https://parsinger.ru/scroll/2/index.html'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')

with webdriver.Chrome(options=chrome_options) as driver:
    driver.get(link)
    answer = 0
    for element in driver.find_elements(By.CLASS_NAME, 'item'):
        element.find_element(By.TAG_NAME, 'input').click()
        try:
            answer += int(element.find_element(By.CSS_SELECTOR, 'div > p > span').text)
        except ValueError:
            pass
    print(answer)
