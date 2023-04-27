import pytest

from ..pages.catalog_page import CatalogPage
from ..pages.locators import CatalogPageLocators


@pytest.mark.catalog_page
class TestCatalogPage:

    def test_compare_button_present(self, driver):
        catalog_page = CatalogPage(driver)
        catalog_page.open()
        assert catalog_page.is_element_present(
            CatalogPageLocators.COMPARE_BUTTON
        ), 'Compare button is not present on catalog page.'

    def test_page_pagination_present(self, driver):
        catalog_page = CatalogPage(driver)
        catalog_page.open()
        assert catalog_page.is_element_present(
            CatalogPageLocators.PAGE_PAGINATION
        ), 'Page pagination is not present on catalog page.'

    def test_sort_by_button_present(self, driver):
        catalog_page = CatalogPage(driver)
        catalog_page.open()
        assert catalog_page.is_element_present(
            CatalogPageLocators.SORT_BY_BUTTON
        ), 'Sort by button is not present on catalog page.'

    def test_show_button_present(self, driver):
        catalog_page = CatalogPage(driver)
        catalog_page.open()
        assert catalog_page.is_element_present(
            CatalogPageLocators.SHOW_BUTTON
        ), 'Show button is not present on catalog page.'

    def test_grid_button_present(self, driver):
        catalog_page = CatalogPage(driver)
        catalog_page.open()
        assert catalog_page.is_element_present(
            CatalogPageLocators.GRID_BUTTON
        ), 'Grid button is not present on catalog page.'
