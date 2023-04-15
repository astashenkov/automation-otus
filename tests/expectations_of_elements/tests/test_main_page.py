import pytest

from ..pages.main_page import MainPage
from ..pages.locators import MainPageLocators


@pytest.mark.main_page
class TestMainPage:
    def test_carousel_banner_present(self, browser):
        main_page = MainPage(browser)
        carousel_banner_locator = MainPageLocators.CAROUSEL_BANNER
        main_page.open()
        assert main_page.is_element_present(carousel_banner_locator), 'Carousel banner is not present on main page.'

    def test_logo_main_present(self, browser):
        main_page = MainPage(browser)
        logo_main = MainPageLocators.LOGO_MAIN
        main_page.open()
        assert main_page.is_element_present(logo_main), 'Logo OpenCart is not present on main page.'

    def test_page_header_present(self, browser):
        main_page = MainPage(browser)
        page_header = MainPageLocators.PAGE_HEADER
        main_page.open()
        assert main_page.is_element_present(page_header), 'Header is not present on main page.'

    def test_cart_items_dropdown_present(self, browser):
        main_page = MainPage(browser)
        cart_items_dropdown = MainPageLocators.CART_ITEMS
        main_page.open()
        assert main_page.is_element_present(cart_items_dropdown), 'Items dropdown is not present on main page.'

    def test_search_input_present(self, browser):
        main_page = MainPage(browser)
        search_input = MainPageLocators.SEARCH_INPUT
        main_page.open()
        assert main_page.is_element_present(search_input), 'Search input is not present on main page.'
