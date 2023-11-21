from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

with webdriver.Chrome() as driver:
    button = driver.find_element(By.ID, 'button')

    actions = ActionChains(driver)  # create class element
    actions.move_to_element(button)  # move cursor to element
    actions.click(button)  # click element
    actions.perform()  # perform listed actions

"""
    actions.drag_and_drop_by_offset(button, -11, 0).perform()  # move element to 100px to the left
    actions.drag_and_drop_by_offset(source, target).perform()
    actions.click_and_hold(button).perform()  # click and hold
    actions.context_click(button).perform()  # right mouse click
    actions.release()  # release mouse click
    actions.release(self, on_element=None)  - default, can replace None with specific element
    actions.key_down(value, element)  # key down without release, to be used with keys-modificators: Control, Alt, Shift
    actions.key_down(Keys.CONTROL, button)
    actions.key_up(value, element)  # release pressed key
    actions.move_by_offset(x, y)  # move cursor
    actions.move_to_element(button)  # move cursor
    actions.move_to_element_with_offset(button, x, y)  # place cursor to (x, y) to the element
    actions.pause(seconds)  # same as sleep
    actions.send_keys(Keys.DOWN)  # send keys to given element
    actions.send_keys_to_element(element, *keys_to_send)  # keys: can be a string or keys (Keys.ENTER)
    actions.reset_actions()  # clear actions queue
    actions.scroll_by_amount(x, y)
    actions.scroll_from_origin(scroll_origin=element, x, y)
    actions.scroll_to_element(element)
"""
