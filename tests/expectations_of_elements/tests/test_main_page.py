import pytest

from ..pages.main_page import MainPage
from ..pages.locators import MainPageLocators


@pytest.mark.main_page
class TestMainPage:
    def test_hero_banner_present(self, browser):
        main_page = MainPage(browser)
        hero_banner_locator = MainPageLocators.HERO_BANNER
        main_page.open()
        assert main_page.is_element_present(hero_banner_locator), 'Hero banner is not present on main page.'

    def test_marketplace_section_present(self, browser):
        main_page = MainPage(browser)
        marketplace_section = MainPageLocators.MARKETPLACE_SECTION
        main_page.open()
        assert main_page.is_element_present(marketplace_section), 'Marketplace section is not present on main page.'

    def test_login_button_present(self, browser):
        main_page = MainPage(browser)
        login_button = MainPageLocators.LOGIN_BUTTON
        main_page.open()
        assert main_page.is_element_present(login_button), 'Login button is not present on main page.'

    def test_register_button_present(self, browser):
        main_page = MainPage(browser)
        register_button = MainPageLocators.REGISTER_BUTTON
        main_page.open()
        assert main_page.is_element_present(register_button), 'Register button is not present on main page.'

    def test_business_section_present(self, browser):
        main_page = MainPage(browser)
        business_section = MainPageLocators.BUSINESS_SECTION
        main_page.open()
        assert main_page.is_element_present(business_section), 'Business section is not present on main page.'
