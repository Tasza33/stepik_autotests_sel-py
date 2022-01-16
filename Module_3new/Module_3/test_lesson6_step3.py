from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium import webdriver
import time
import math


@pytest.fixture(scope="class")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestStepikPages:
    @pytest.mark.parametrize('url', [
        "https://stepik.org/lesson/236895/step/1",
        "https://stepik.org/lesson/236896/step/1",
        "https://stepik.org/lesson/236897/step/1",
        "https://stepik.org/lesson/236898/step/1",
        "https://stepik.org/lesson/236899/step/1",
        "https://stepik.org/lesson/236903/step/1",
        "https://stepik.org/lesson/236904/step/1",
        "https://stepik.org/lesson/236905/step/1"
    ])
    def test_putting_text_into_textarea(self, browser, url):
        link = f"{url}"
        browser.get(link)
        answer = math.log(int(time.time()))
        textarea = browser.find_element_by_tag_name("textarea")
        textarea.send_keys((str(answer)))

        button = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
        )
        button.click()

        text_result = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint"))
        )

        assert text_result.text == "Correct!", print(text_result.text)
