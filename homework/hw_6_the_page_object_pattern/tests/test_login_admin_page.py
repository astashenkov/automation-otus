import pytest

from ..pages.login_to_admin_page import LoginToAdminPage
from ..pages.locators import LoginAdminPageLocators


@pytest.mark.login_to_admin_page
class TestLoginToAdminPage:

    def test_first_name_input_present(self, driver):
        login_to_admin_page = LoginToAdminPage(driver)
        login_to_admin_page.open()
        assert login_to_admin_page.is_element_present(
            LoginAdminPageLocators.FIRST_NAME_INPUT
        ), 'First name input is not present on login to admin page.'

    def test_password_input_present(self, driver):
        login_to_admin_page = LoginToAdminPage(driver)
        login_to_admin_page.open()
        assert login_to_admin_page.is_element_present(
            LoginAdminPageLocators.PASSWORD_INPUT
        ), 'Password input is not present on login to admin page.'

    def test_login_button_present(self, driver):
        login_to_admin_page = LoginToAdminPage(driver)
        login_to_admin_page.open()
        assert login_to_admin_page.is_element_present(
            LoginAdminPageLocators.LOGIN_BUTTON
        ), 'Login button is not present on login to admin page.'

    def test_forgot_password_button_present(self, driver):
        login_to_admin_page = LoginToAdminPage(driver)
        login_to_admin_page.open()
        assert login_to_admin_page.is_element_present(
            LoginAdminPageLocators.FORGOT_PASSWORD
        ), 'Forgot password button is not present on login to admin page.'

    def test_opencart_link_present(self, driver):
        login_to_admin_page = LoginToAdminPage(driver)
        login_to_admin_page.open()
        assert login_to_admin_page.is_element_present(
            LoginAdminPageLocators.OPENCART_LINK
        ), 'Opencart link is not present on login to admin page.'
