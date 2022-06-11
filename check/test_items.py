
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_items_button_add_to_card(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    button = WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.btn-primary')))
    assert button, 'Кнопка отсутствует на сайте'


if __name__ == "__main__":
    pytest.main()
