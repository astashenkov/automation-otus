import pytest

from ..pages.login_to_admin_page import LoginToAdminPage
from ..pages.locators import LoginAdminPage


@pytest.mark.login_to_admin_page
class TestLoginToAdminPage:

    def test_first_name_input_present(self, browser):
        login_to_admin_page = LoginToAdminPage(browser)
        first_name_input = LoginAdminPage.FIRST_NAME_INPUT
        login_to_admin_page.open()
        assert login_to_admin_page.is_element_present(
            first_name_input
        ), 'First name input is not present on login to admin page.'

    def test_password_input_present(self, browser):
        login_to_admin_page = LoginToAdminPage(browser)
        password_input = LoginAdminPage.PASSWORD_INPUT
        login_to_admin_page.open()
        assert login_to_admin_page.is_element_present(
            password_input
        ), 'Password input is not present on login to admin page.'

    def test_login_button_present(self, browser):
        login_to_admin_page = LoginToAdminPage(browser)
        login_button = LoginAdminPage.LOGIN_BUTTON
        login_to_admin_page.open()
        assert login_to_admin_page.is_element_present(
            login_button
        ), 'Login button is not present on login to admin page.'

    def test_forgot_password_button_present(self, browser):
        login_to_admin_page = LoginToAdminPage(browser)
        forgot_password = LoginAdminPage.FORGOT_PASSWORD
        login_to_admin_page.open()
        assert login_to_admin_page.is_element_present(
            forgot_password
        ), 'Forgot password button is not present on login to admin page.'

    def test_opencart_link_present(self, browser):
        login_to_admin_page = LoginToAdminPage(browser)
        opencart_link = LoginAdminPage.OPENCART_LINK
        login_to_admin_page.open()
        assert login_to_admin_page.is_element_present(
            opencart_link
        ), 'Opencart link is not present on login to admin page.'
