import os

import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def if_exists_then_remove(filename):
    if os.path.exists(filename):
        os.remove(filename)


def get_element_ec(wait_time, by_element):
    try:
        element = WebDriverWait(wd, wait_time).until(EC.element_to_be_clickable(by_element))
        return element
    except selenium.common.exceptions.TimeoutException:
        wd.quit()


def fill_form():
    input_element = get_element_ec(5, (By.CSS_SELECTOR, '.exportInput'))
    input_element.send_keys('Сергієнко Андрій')


def submit():
    submit_button = wd.find_element(By.CLASS_NAME, "freebirdFormviewerViewNavigationSubmitButton")
    submit_button.click()


def screenshot(filename):
    if_exists_then_remove(filename)
    wd.save_screenshot(filename)


wd = webdriver.Chrome()
wd.get('https://docs.google.com/forms/d/e/1FAIpQLScLhHgD5pMnwxl8JyRfXXsJekF8_pDG36XtSEwaGsFdU2egyw/viewform')

elements = wd.find_elements(By.CSS_SELECTOR, '.freebirdFormviewerViewNumberedItemContainer')
for element in elements:
    if element.find_element(By.CSS_SELECTOR, '.exportItemTitle').text == "Введіть ваше ім'я *":
        fill_form()
        screenshot('screenshot1.png')
        submit()
        screenshot('screenshot2.png')
        break
wd.quit()





