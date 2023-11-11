import time
from selenium import webdriver
from selenium.webdriver.common.by import By

proxy = '8.210.83.33:80'
url = 'https://2ip.ru/'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=%s' % proxy)

with webdriver.Chrome(options=chrome_options) as browser:
    browser.get(url)
    print(browser.find_element(By.ID, 'd_clip_button').find_element(By.TAG_NAME, 'span').text)
    time.sleep(5)

# >>> 95.27.00.01


# proxy with authorisation:

import time
from selenium.webdriver.common.by import By
from seleniumwire import webdriver

options = {'proxy': {
    'http': "socks5://D2Frs6:75JjrW@194.28.210.39:9867",
    'https': "socks5://D2Frs6:75JjrW@194.28.210.39:9867",
    }}

url = 'https://2ip.ru/'

with webdriver.Chrome(seleniumwire_options=options) as browser:
    browser.get(url)
    print(browser.find_element(By.ID, 'd_clip_button').find_element(By.TAG_NAME, 'span').text)
    time.sleep(5)
