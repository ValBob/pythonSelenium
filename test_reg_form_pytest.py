from selenium import webdriver
import time


def test_1():
    pass


def test_2():
    link = 'http://suninjuly.github.io/registration2.html'
    browser = webdriver.Chrome()
    browser.get(link)

    # Fill the form
    name_input = browser.find_element_by_xpath('//div[@class="first_block"]/div/input[contains(@class, "first")]')
    name_input.send_keys("Ivan")
    surname_input = browser.find_element_by_xpath(
        '//div[@class="first_block"]/div/input[contains(@class, "second")]')
    surname_input.send_keys("Ivanov")
    email_input = browser.find_element_by_xpath('//div[@class="first_block"]/div/input[contains(@class, "third")]')
    email_input.send_keys("+7(999)-999-99-99")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # time for page to load
    time.sleep(5)

    # name for test log-file
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    assert welcome_text == "Congratulations! You have successfully registered!", "NoSuchElementException"
