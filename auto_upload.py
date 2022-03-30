import time
from selenium import webdriver

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")
    name = browser.find_element_by_css_selector("[name='firstname']")
    name.send_keys("kate")
    surname = browser.find_element_by_css_selector("[name='lastname']")
    surname.send_keys("smith")
    email = browser.find_element_by_css_selector("[name='email']")
    email.send_keys("kate@example.com")
    browser.find_element_by_id("file").send_keys(r"C:\Users\gefes\PycharmProjects\pythonSelenium\test.txt")
    browser.find_element_by_tag_name("button").click()

finally:
    time.sleep(10)
    browser.quit()
