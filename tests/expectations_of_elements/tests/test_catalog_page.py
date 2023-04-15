import pytest

from ..pages.catalog_page import CatalogPage
from ..pages.locators import CatalogPageLocators


@pytest.mark.catalog_page
class TestCatalogPage:

    def test_compare_button_present(self, browser):
        catalog_page = CatalogPage(browser)
        compare_button = CatalogPageLocators.COMPARE_BUTTON
        catalog_page.open()
        assert catalog_page.is_element_present(
            compare_button
        ), 'Compare button is not present on catalog page.'

    def test_page_pagination_present(self, browser):
        catalog_page = CatalogPage(browser)
        page_pagination = CatalogPageLocators.PAGE_PAGINATION
        catalog_page.open()
        assert catalog_page.is_element_present(
            page_pagination
        ), 'Page pagination is not present on catalog page.'

    def test_sort_by_button_present(self, browser):
        catalog_page = CatalogPage(browser)
        sort_by_button = CatalogPageLocators.SORT_BY_BUTTON
        catalog_page.open()
        assert catalog_page.is_element_present(
            sort_by_button
        ), 'Sort by button is not present on catalog page.'

    def test_show_button_present(self, browser):
        catalog_page = CatalogPage(browser)
        show_button = CatalogPageLocators.SHOW_BUTTON
        catalog_page.open()
        assert catalog_page.is_element_present(
            show_button
        ), 'Show button is not present on catalog page.'

    def test_grid_button_present(self, browser):
        catalog_page = CatalogPage(browser)
        grid_button = CatalogPageLocators.GRID_BUTTON
        catalog_page.open()
        assert catalog_page.is_element_present(
            grid_button
        ), 'Grid button is not present on catalog page.'
