from pprint import pprint
from selenium import webdriver

options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument('--headless')


with webdriver.Chrome(options=options_chrome) as webdriver:
    webdriver.get('https://ya.ru/')
    cookies = webdriver.get_cookies()
    pprint(cookies)

# pprint module provides a capability to “pretty -print” arbitrary Python data structures
# in a form which can be used as input to the interpreter

    for cookie in cookies:
        print(cookie['name'])  # or cookie['value'] to get value

    print(webdriver.get_cookie('bh')['expiry'])
