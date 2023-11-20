from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver import Keys

with webdriver.Chrome() as driver:
    driver.get('http://parsinger.ru/scroll/1')

    # key down
    ActionChains(driver).key_down(Keys.SHIFT).send_keys('abc').perform()

    # key up
    ActionChains(driver).key_down(Keys.SHIFT).send_keys('a').key_up(Keys.SHIFT).send_keys('b').perform()

    # simulate tab
    driver.find_element(By.TAG_NAME, 'input').send_keys(Keys.TAB)

    # simulate down button
    driver.find_element(By.TAG_NAME, 'input').send_keys(Keys.DOWN)

    # other buttons:
    # ADD, ALT, ARROW_DOWN/LEFT/RIGHT/UP, BACKSPACE, CANCEL, DELETE, UP, DOWN, ENTER, ESCAPE, F1/2..., INSERT, SPACE,...
    