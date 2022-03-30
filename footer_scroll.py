import time
import math
from selenium import webdriver

try:
    browser = webdriver.Chrome()
    browser.get("http://SunInJuly.github.io/execute_script.html")
    x = browser.find_element_by_id("input_value").text
    res = math.log(abs(12 * math.sin(int(x))))
    browser.find_element_by_id("answer").send_keys(str(res))
    browser.find_element_by_id('robotCheckbox').click()
    browser.execute_script("window.scrollBy(0, 150);")
    browser.find_element_by_id('robotsRule').click()
    button = browser.find_element_by_tag_name("button").click()
    button.click()
finally:
    time.sleep(10)
    browser.quit()
