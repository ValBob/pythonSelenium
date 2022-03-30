import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/selects1.html')
    time.sleep(1)
    num1 = browser.find_element_by_id("num1").text
    num2 = browser.find_element_by_id("num2").text
    res = int(num1) + int(num2)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(res))
    browser.find_element_by_tag_name("button").click()
finally:
    time.sleep(10)
    browser.quit()
