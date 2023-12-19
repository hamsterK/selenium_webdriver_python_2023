from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument('--start-maximized')
options_chrome.add_argument('--force-device-scale-factor=1')

with webdriver.Chrome(options=options_chrome) as driver:
    driver.maximize_window()
    driver.get('https://parsinger.ru/selenium/5.10/6/index.html')
    actions = ActionChains(driver)

    sliders = driver.find_elements(By.CLASS_NAME, "slider-container")
    for slider_container in sliders:
        slider = slider_container.find_element(By.CLASS_NAME, 'volume-slider')

        target_value = int(slider_container.find_element(By.CLASS_NAME, 'target-value').text)
        current_value = int(slider.get_attribute("value"))

        while current_value != target_value:
            if current_value < target_value:
                slider.send_keys(Keys.ARROW_RIGHT)
            else:
                slider.send_keys(Keys.ARROW_LEFT)
            current_value = int(slider.get_attribute("value"))

    print(driver.find_element(By.ID, "message").text)
