import pytest

from ..pages.registration_page import RegistrationPage
from ..pages.locators import RegisterPageLocators


@pytest.mark.registration_page
class TestRegistrationPage:

    def test_first_name_input_present(self, browser):
        registration_page = RegistrationPage(browser)
        first_name_input = RegisterPageLocators.FIRST_NAME_INPUT
        registration_page.open()
        assert registration_page.is_element_present(
            first_name_input
        ), 'First name input is not present on registration page.'

    def test_last_name_input_present(self, browser):
        registration_page = RegistrationPage(browser)
        last_name_input = RegisterPageLocators.LAST_NAME_INPUT
        registration_page.open()
        assert registration_page.is_element_present(
            last_name_input
        ), 'Last name input is not present on registration page.'

    def test_email_input_present(self, browser):
        registration_page = RegistrationPage(browser)
        email_input = RegisterPageLocators.EMAIL_INPUT
        registration_page.open()
        assert registration_page.is_element_present(
            email_input
        ), 'Email input is not present on registration page.'

    def test_password_input_present(self, browser):
        registration_page = RegistrationPage(browser)
        password_input = RegisterPageLocators.PASSWORD_INPUT
        registration_page.open()
        assert registration_page.is_element_present(
            password_input
        ), 'Password input is not present on registration page.'

    def test_submit_button_present(self, browser):
        registration_page = RegistrationPage(browser)
        submit_button = RegisterPageLocators.SUBMIT_BUTTON
        registration_page.open()
        assert registration_page.is_element_present(
            submit_button
        ), 'Submit button is not present on registration page.'
