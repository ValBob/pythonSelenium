import time
import math
from selenium import webdriver

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/math.html')
    time.sleep(1)
    x = browser.find_element_by_css_selector("#input_value").text
    res = str(math.log(abs(12 * math.sin(int(x)))))
    answer = browser.find_element_by_css_selector("#answer")
    answer.send_keys(res)
    browser.find_element_by_css_selector('#robotCheckbox').click()
    browser.find_element_by_css_selector('#robotsRule').click()
    browser.find_element_by_css_selector('button[type="submit"]').click()
finally:
    time.sleep(10)
    browser.quit()
