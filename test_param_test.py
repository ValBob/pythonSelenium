import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


link_list = [
    'https://stepik.org/lesson/236895/step/1',
    'https://stepik.org/lesson/236896/step/1',
    'https://stepik.org/lesson/236897/step/1',
    'https://stepik.org/lesson/236898/step/1',
    'https://stepik.org/lesson/236899/step/1',
    'https://stepik.org/lesson/236903/step/1',
    'https://stepik.org/lesson/236904/step/1',
    'https://stepik.org/lesson/236905/step/1'
]


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    yield browser
    time.sleep(10)
    browser.quit()


@pytest.mark.parametrize('link', link_list)
def test_correct_answer_by_time(browser, link):
    browser.get(link)
    textarea = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.TAG_NAME, "textarea")))
    answer = math.log(int(time.time()))
    textarea.send_keys(str(answer))
    button = WebDriverWait(browser, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission")))
    button.click()

