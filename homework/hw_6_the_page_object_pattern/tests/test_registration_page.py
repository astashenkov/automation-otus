import pytest

from ..pages.registration_page import RegistrationPage
from ..pages.locators import RegisterPageLocators


@pytest.mark.registration_page
class TestRegistrationPage:

    def test_first_name_input_present(self, driver):
        registration_page = RegistrationPage(driver)
        registration_page.open()
        assert registration_page.is_element_present(
            RegisterPageLocators.FIRST_NAME_INPUT
        ), 'First name input is not present on registration page.'

    def test_last_name_input_present(self, driver):
        registration_page = RegistrationPage(driver)
        registration_page.open()
        assert registration_page.is_element_present(
            RegisterPageLocators.LAST_NAME_INPUT
        ), 'Last name input is not present on registration page.'

    def test_email_input_present(self, driver):
        registration_page = RegistrationPage(driver)
        registration_page.open()
        assert registration_page.is_element_present(
            RegisterPageLocators.EMAIL_INPUT
        ), 'Email input is not present on registration page.'

    def test_password_input_present(self, driver):
        registration_page = RegistrationPage(driver)
        registration_page.open()
        assert registration_page.is_element_present(
            RegisterPageLocators.PASSWORD_INPUT
        ), 'Password input is not present on registration page.'

    def test_submit_button_present(self, driver):
        registration_page = RegistrationPage(driver)
        registration_page.open()
        assert registration_page.is_element_present(
            RegisterPageLocators.SUBMIT_BUTTON
        ), 'Submit button is not present on registration page.'
