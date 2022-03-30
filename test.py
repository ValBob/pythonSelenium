from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


browser = webdriver.Chrome()

# Message: no such element: Unable to locate element: {"method":"css selector","selector":"[id="verify_message"]"}
# browser.implicitly_wait(5)  # Wait for element up to 5 s


browser.get("http://suninjuly.github.io/wait2.html")
# button = browser.find_element_by_id("verify")
button = WebDriverWait(browser, 5).until(
    EC.element_to_be_clickable((By.ID, "verify"))
)
button.click()
message = browser.find_element_by_id("verify_message")

assert "successful" in message.text

