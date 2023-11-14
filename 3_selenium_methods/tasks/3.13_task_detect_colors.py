from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'https://parsinger.ru/selenium/5.5/5/1.html'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')

with webdriver.Chrome(options=chrome_options) as driver:
    driver.get(link)
    for element in driver.find_elements(By.XPATH, '//div[@id="main-container"]/div'):
        target_color = element.find_element(By.TAG_NAME, 'span').text
        element.find_element(By.CSS_SELECTOR, f'select option[value="{target_color}"]').click()
        element.find_element(By.CSS_SELECTOR, f'div>button[data-hex="{target_color}"]').click()
        element.find_element(By.CSS_SELECTOR, 'input[type="checkbox"]').click()
        element.find_element(By.CSS_SELECTOR, 'input[type="text"]').send_keys(target_color)
        element.find_element(By.XPATH, './button').click()
    driver.find_element(By.CSS_SELECTOR, 'body > button').click()
    print(driver.switch_to.alert.text)
