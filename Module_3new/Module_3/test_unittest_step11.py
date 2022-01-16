import unittest
from selenium import webdriver


class test_class_name(unittest.TestCase):

    def test_registration1(self):

        link = "http://suninjuly.github.io/registration1.html"

        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element_by_css_selector('input.form-control.first[required]')
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector('input.form-control.second[required]')
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector('input.form-control.third[required]')
        input3.send_keys("test@test.com")

        button = browser.find_element_by_class_name("btn.btn-default")
        button.click()

        welcome_text_elt = browser.find_element_by_tag_name("h1")

        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "text doesn't match")

    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"

        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element_by_css_selector('input.form-control.first[required]')
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector('input.form-control.second[required]')
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector('input.form-control.third[required]')
        input3.send_keys("test@test.com")

        button = browser.find_element_by_class_name("btn.btn-default")
        button.click()

        welcome_text_elt = browser.find_element_by_tag_name("h1")

        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "text doesn't match")


if __name__ == "__main__":
    unittest.main()
