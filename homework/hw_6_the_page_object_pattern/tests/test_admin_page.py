from ..pages.login_to_admin_page import LoginToAdminPage
from ..pages.locators import AdminPage
import time


def test_add_new_product_in_admin_page(driver):
    login_to_admin_page = LoginToAdminPage(driver)
    login_to_admin_page.open()
    admin_page = login_to_admin_page.login()
    time.sleep(1)
    admin_page.open_products_page()
    time.sleep(10)
    assert admin_page.is_element_present(AdminPage.ADD_NEW_BUTTON), '"Add" button is not presented!'
    time.sleep(10)
