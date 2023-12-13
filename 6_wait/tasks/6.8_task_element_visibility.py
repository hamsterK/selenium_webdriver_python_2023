"""from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'https://parsinger.ru/selenium/5.9/3/index.html'

ids_to_find = ['xhkVEkgm', 'QCg2vOX7', '8KvuO5ja', 'CFoCZ3Ze', '8CiPCnNB', 'XuEMunrz', 'vmlzQ3gH', 'axhUiw2I',
               'jolHZqD1', 'ZM6Ms3tw', '25a2X14r', 'aOSMX9tb', 'YySk7Ze3', 'QQK13iyY', 'j7kD7uIR']

with webdriver.Chrome() as driver:
    driver.get(link)
    while True:
        try:
            print(driver.switch_to.alert.text)
        except:
            for i in ids_to_find:
                try:
                    driver.find_element(By.ID, i).click()
                except:
                    pass
        try:
            print(driver.switch_to.alert.text)
            break
        except:
            continue
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

URL = "https://parsinger.ru/selenium/5.9/3/index.html"
IDS = ('xhkVEkgm', 'QCg2vOX7', '8KvuO5ja', 'CFoCZ3Ze', '8CiPCnNB',
       'XuEMunrz', 'vmlzQ3gH', 'axhUiw2I', 'jolHZqD1', 'ZM6Ms3tw',
       '25a2X14r', 'aOSMX9tb', 'YySk7Ze3', 'QQK13iyY', 'j7kD7uIR')


def make_box_locator(box_id) -> tuple[str, str]:
    return By.CSS_SELECTOR, f".box[id='{box_id}']"


def wait_quiz() -> str:
    with webdriver.Chrome() as browser:
        browser.get(URL)
        box_locators = (make_box_locator(box_id) for box_id in IDS)
        for loc in box_locators:
            WebDriverWait(browser, 100).until(EC.visibility_of_element_located(loc)).click()
        return browser.switch_to.alert.text


print(wait_quiz())