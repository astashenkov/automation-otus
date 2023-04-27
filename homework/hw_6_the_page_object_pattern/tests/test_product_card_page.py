import pytest

from ..pages.product_card_page import ProductCardPage
from ..pages.locators import ProductCardPageLocators


@pytest.mark.product_card_page
class TestProductCardPage:

    def test_product_image_present(self, browser):
        product_card_page = ProductCardPage(browser)
        product_card_page.open()
        assert product_card_page.is_element_present(
            ProductCardPageLocators.PRODUCT_IMAGE
        ), 'Product image is not present on product card page.'

    def test_add_to_cart_button_present(self, browser):
        product_card_page = ProductCardPage(browser)
        product_card_page.open()
        assert product_card_page.is_element_present(
            ProductCardPageLocators.ADD_TO_CART_BUTTON
        ), 'Add to cart button is not present on product card page.'

    def test_quantity_input_present(self, browser):
        product_card_page = ProductCardPage(browser)
        product_card_page.open()
        assert product_card_page.is_element_present(
            ProductCardPageLocators.QUANTITY_INPUT
        ), 'Quantity input is not present on product card page.'

    def test_options_dropdown_present(self, browser):
        product_card_page = ProductCardPage(browser)
        product_card_page.open()
        assert product_card_page.is_element_present(
            ProductCardPageLocators.OPTIONS_DROPDOWN
        ), 'Options dropdown is not present on product card page.'

    def test_grid_button_present(self, browser):
        product_card_page = ProductCardPage(browser)
        product_card_page.open()
        assert product_card_page.is_element_present(
            ProductCardPageLocators.DESCRIPTION_TAB
        ), 'Description tab is not present on product card page.'
