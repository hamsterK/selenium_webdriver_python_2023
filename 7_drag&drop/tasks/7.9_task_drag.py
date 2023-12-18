from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

link = 'https://parsinger.ru/selenium/5.10/4/index.html'

options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument('--start-maximized')
options_chrome.add_argument('--force-device-scale-factor=1')

with webdriver.Chrome(options=options_chrome) as driver:
    driver.get(link)
    action = ActionChains(driver)
    for element in driver.find_elements(By.CSS_SELECTOR, 'div.basket_with_toys>div'):
        element_color = str(element.get_attribute('class').split()[1]).split('_')[0]
        for basket in driver.find_elements(By.CSS_SELECTOR, 'div.main_container>div'):
            if element_color in basket.get_attribute('class'):
                action.drag_and_drop(element, basket).perform()
    print(driver.find_element(By.CLASS_NAME, 'message').text)
