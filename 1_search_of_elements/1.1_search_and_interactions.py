from selenium import webdriver
from selenium.webdriver.common.by import By


url = 'http://parsinger.ru/selenium/3/3.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    elem = browser.find_element(By.CLASS_NAME, 'text')
    print(elem)

    # By options: ID, CSS_SELECTOR, XPATH, NAME, TAG_NAME, CLASS_NAME, LINK_TEXT, PARTIAL_LINK_TEXT
    # driver.find_element => element (if not found => NoSuchElementException) / driver.find_elements => list
    # to read WebElement(find_element_ => driver.find_element.text

    # actions: click(), send_keys('input_info'), get_attribute('href(to get links)'), text (get visible text)
    # browser.find_element(By.ID, "some_button_id").click()
    