"""
.set_window_size(x, y)  # min = (516, 134)
.get_window_size()
.get_window_size().get('height')
== .get_window_size()["height"]
.get_window_size().get('width')
== get_window_size()["width"]
"""

from selenium import webdriver

with webdriver.Chrome() as driver:
    driver.get('http://parsinger.ru/window_size/1/')
    driver.set_window_size(1200, 720)
    print(driver.get_window_size().get('height'))
    print(driver.get_window_size().get('width'))
