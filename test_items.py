link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_button_add_to_basket_present(browser):
    browser.get(link)
    add_button = browser.find_elements_by_class_name('btn-add-to-basket')
    assert add_button, 'basket button not found'
