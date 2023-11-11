"""
navigation in history:

webdriver.back()
webdriver.forward()
webdriver.refresh()


screenshots:

webdriver.get_screenshot_as_file('.../file_name.jpg') => returns True if successful, otherwise False
webdriver.save_screenshot('file_name.jpg') => save in project directory
webdriver.get_screenshot_as_png() => save as binary data
webdriver.get_screenshot_as_base64() => codec Base64

browser:

webdriver.get(url)
webdriver.quit() - close all tabs/windows/processes
webdriver.close - close current tab

javascript:

webdriver.execute_script('script')
webdriver.execute_async_script('script', *args)

await:

webdriver.set_page_load_timeout() - returns exception if time is out before the page is loaded
webdriver.implicitly_wait(10)
webdriver.WebDriverWait(driver, timeout).until(condition)

search_elements:

webdriver.find_element(By.ID, 'ID') => 1st element found (if not found => NoSuchElementException)
webdriver.find_elements(By.ID, 'ID') => list

browser_window:

webdriver.get_window_position() => returns current position of browser window
webdriver.maximize_window()
webdriver.minimize_window()
webdriver.fullscreen_window() => F11
webdriver.get_window_size() => ({'width': 945, 'height': 1020})
webdriver.set_window_size(800,600)

cookies

webdriver.get_cookies() => list of all cookeis
webdriver.get_cookie(name)
webdriver.add_cookie(cookie_dict)
webdriver.delete_cookie(name)
webdriver.delete_all_cookies() => delete all cookies for ongoing session

elements:

element.click()
element.send_keys('text') - text input
element.clear()
element.is_displayed()
element.is_enabled()
element.is_selected() => radiobuttons, checkboxes
element.get_attribute('attribute') => return value of desired attribute
element.text => return text of the element
element.submit() => submit form in which given element is present

frames:

webdriver.switch_to.frame('name') => move focus to selected frame
webdriver.switch_to.default_content() => return focus to main content of the page

alerts:

webdriver.switch_to.alert => change focus to browser alert

"""