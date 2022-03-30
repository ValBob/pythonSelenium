from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elems = browser.find_elements_by_tag_name("input")
    for elem in elems:
        elem.send_keys("bla")

    btn = browser.find_element_by_css_selector("button.btn")
    btn.click()

finally:
    time.sleep(30)
    browser.quit()
