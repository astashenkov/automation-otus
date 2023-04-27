import pytest

from ..pages.main_page import MainPage
from ..pages.locators import MainPageLocators


@pytest.mark.main_page
class TestMainPage:
    def test_carousel_banner_present(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        assert main_page.is_element_present(
            MainPageLocators.CAROUSEL_BANNER
        ), 'Carousel banner is not present on main page.'

    def test_logo_main_present(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        assert main_page.is_element_present(
            MainPageLocators.LOGO_MAIN
        ), 'Logo OpenCart is not present on main page.'

    def test_page_header_present(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        assert main_page.is_element_present(
            MainPageLocators.PAGE_HEADER
        ), 'Header is not present on main page.'

    def test_cart_items_dropdown_present(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        assert main_page.is_element_present(
            MainPageLocators.CART_ITEMS
        ), 'Items dropdown is not present on main page.'

    def test_search_input_present(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        assert main_page.is_element_present(
            MainPageLocators.SEARCH_INPUT
        ), 'Search input is not present on main page.'
