import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from webcolors import rgb_to_name


options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')  # maximizes window
options.add_argument("--force-device-scale-factor=1")  # web content is displayed at its native, unscaled resolution

with webdriver.Chrome(options=options) as driver:
    driver.get('https://parsinger.ru/selenium/5.10/3/index.html')
    time.sleep(3)
    action = ActionChains(driver)

    boxes = driver.find_elements(By.CLASS_NAME, 'draganddrop')
    boxends = driver.find_elements(By.CLASS_NAME, 'draganddrop_end')
    for box in boxes:
        c_box = box.get_attribute('style')
        c_box = rgb_to_name(tuple(map(int, c_box[c_box.find('(') + 1: c_box.find(')')].split(', '))),
                            spec='css3') if 'rgb' in c_box else c_box.split(' ', 1)[1].split(';')[0]
        for boxend in boxends:
            c_boxend = boxend.get_attribute('style').split(' ', 1)[1]
            c_boxend = c_boxend[0: c_boxend.find(';')]
            if c_box == c_boxend:
                action.drag_and_drop(box, boxend).release().perform()
    print(driver.find_element(By.ID, 'message').text)
    