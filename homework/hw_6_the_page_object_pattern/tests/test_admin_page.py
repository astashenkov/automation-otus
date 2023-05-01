import pytest

from ..pages.login_to_admin_page import LoginToAdminPage


@pytest.mark.admin_page
class TestAdminPage:
    def test_delete_product_from_admin_page(self, driver):
        login_to_admin_page = LoginToAdminPage(driver)
        login_to_admin_page.open()
        admin_page = login_to_admin_page.login()
        admin_page.open_products_page()
        deleted_product_title = admin_page.delete_upper_product()
        assert deleted_product_title != admin_page.upper_product_title, 'Product has not been removed'

    def test_create_product_from_admin_page(self, driver):
        login_to_admin_page = LoginToAdminPage(driver)
        login_to_admin_page.open()
        admin_page = login_to_admin_page.login()
        admin_page.open_products_page()
        admin_page.create_new_product()
        admin_page.open_products_page()
