from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get('http://parsinger.ru/expectations/2/index.html')
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'btn'))).click()
    element = WebDriverWait(driver, 10).until(EC.title_is('title changed'))
    #  element = WebDriverWait(browser, 10).until(EC.title_contains('tle'))
    print(element)

"""
EC.title_is(title: str)
EC.title_contains(title: str)
EC.url_contains(url: str)
EC.url_matches(pattern: str) - regex
EC.url_to_be(url: str)
EC.url_changes(url: str)

EC.presence_of_element_located(locator) != visible (might have 'display: none' or 'visibility: hidden')
EC.visibility_of_element_located(locator)
EC.visibility_of(element) - element, not locator
EC.presence_of_all_elements_located(locator)
EC.visibility_of_any_elements_located(locator)
EC.visibility_of_all_elements_located(locator)

EC.text_to_be_present_in_element(locator, text_)
EC.text_to_be_present_in_element_value(locator, text_) - in value attribute of the element
EC.text_to_be_present_in_element_attribute(locator, attribute_, text_) - attribute_name
EC.element_attribute_to_include(locator, attribute_)

EC.frame_to_be_available_and_switch_to_it(locator) + automatic switch to it
EC.invisibility_of_element_located(locator)
EC.invisibility_of_element(element)
EC.element_to_be_clickable(mark)
EC.staleness_of(element) - True if not present on DOM any more or its state is outdated (example - link)
EC.element_to_be_selected(element) - if already selected
EC.element_located_to_be_selected(locator)
EC.element_selection_state_to_be(element, is_selected) - is selected
EC.element_located_selection_state_to_be(locator, is_selected)
EC.number_of_windows_to_be(num_windows)
EC.new_window_is_opened(current_handles) - compares with given list of windows identifiers
EC.alert_is_present() - automatic return of alert object
"""
