import pytest

from ..pages.main_page import MainPage
from ..pages.locators import MainPageLocators


@pytest.mark.main_page
class TestMainPage:
    def test_hero_banner_present(self, browser):
        main_page = MainPage(browser)
        hero_banner_locator = MainPageLocators.HERO_BANNER
        support_section = MainPageLocators.SUPPORT_SECTION
        main_page.open()
        assert main_page.is_element_present(hero_banner_locator), 'Hero banner is not present on main page.'
        assert main_page.is_element_present(support_section), 'Support section is not present on main page.'

    def test_support_section_present(self, browser):
        main_page = MainPage(browser)
        support_section = MainPageLocators.SUPPORT_SECTION
        main_page.open()
        assert main_page.is_element_present(support_section), 'Support section is not present on main page.'
