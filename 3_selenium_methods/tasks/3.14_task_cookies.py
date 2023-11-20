from selenium import webdriver

link = 'https://parsinger.ru/methods/3/index.html'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')

with webdriver.Chrome() as driver:
    driver.get(link)
    cookies = driver.get_cookies()
    print(sum(int(cookie['value']) for cookie in cookies if cookie['name'].startswith('secret_cookie_')))
