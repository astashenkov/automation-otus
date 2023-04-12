from ..pages.registration_page import RegistrationPage


class TestRegistrationPage:

    def test_foo(self, browser):
        registration_page = RegistrationPage(browser)
        registration_page.open()
