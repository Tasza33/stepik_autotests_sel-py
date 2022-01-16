link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_button_add_to_basket_present(browser):
    browser.get(link)
    assert browser.find_element_by_class_name('btn-add-to-basket').is_enabled(), \
        'basket button not found'


