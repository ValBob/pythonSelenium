import time
import math
from selenium import webdriver

try:
    browser = webdriver.Chrome()
    # browser.get("http://suninjuly.github.io/alert_accept.html")  # switch to alert
    browser.get("http://suninjuly.github.io/redirect_accept.html")
    browser.find_element_by_tag_name("button").click()
    # browser.switch_to.alert.accept()  # switch to alert
    browser.switch_to.window(browser.window_handles[1])
    time.sleep(1)
    x = browser.find_element_by_css_selector("#input_value").text
    res = str(math.log(abs(12 * math.sin(int(x)))))
    answer = browser.find_element_by_css_selector("#answer")
    answer.send_keys(res)
    browser.find_element_by_tag_name('button').click()
finally:
    time.sleep(10)
    browser.quit()
