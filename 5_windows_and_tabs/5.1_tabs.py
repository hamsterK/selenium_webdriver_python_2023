"""
.current_window_handle  # descriptor (= identificator) of cyrrent tab
.window_handles  # returns list of all open tabs' descriptors
.switch_to.window(window_handles[0])  # switch focus between tabs
.execute_script("return document.title;")  # get title of the tab
== driver.title
"""

import time
from selenium import webdriver

with webdriver.Chrome() as driver:
    result = []
    driver.get('http://parsinger.ru/blank/2/1.html')
    time.sleep(1)

    driver.execute_script('window.open("http://parsinger.ru/blank/2/2.html", "_blank1");')
    driver.execute_script('window.open("http://parsinger.ru/blank/2/3.html", "_blank2");')
    driver.execute_script('window.open("http://parsinger.ru/blank/2/4.html", "_blank3");')
    time.sleep(2)
    print(driver.window_handles)
