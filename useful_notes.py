import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromiumService

# auto download of latest webdriver
with webdriver.Chrome(service=ChromiumService(ChromeDriverManager().install())) as driver:
    driver.get("https://stepik.org/a/104774")
    time.sleep(5)

# close / vs quit
driver.close()  # close current browser window
driver.quit()  # close all windows initiated by webdriver in current session

