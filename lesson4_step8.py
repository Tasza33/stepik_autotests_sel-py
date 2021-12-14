from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

from selenium import webdriver

try:

    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    price = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
         )

    button1 = browser.find_element_by_id('book').click()

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    answer = browser.find_element_by_tag_name("input").send_keys(y)

    button2 = browser.find_element_by_id("solve")

    button2.click()

finally:

    time.sleep(30)
    browser.quit()
