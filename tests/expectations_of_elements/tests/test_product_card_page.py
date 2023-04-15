import pytest

from ..pages.product_card_page import ProductCardPage
from ..pages.locators import ProductCardPageLocators


@pytest.mark.product_card_page
class TestProductCardPage:

    def test_product_image_present(self, browser):
        product_card_page = ProductCardPage(browser)
        product_image = ProductCardPageLocators.PRODUCT_IMAGE
        product_card_page.open()
        assert product_card_page.is_element_present(
            product_image
        ), 'Product image is not present on product card page.'

    def test_add_to_cart_button_present(self, browser):
        product_card_page = ProductCardPage(browser)
        add_to_cart_button = ProductCardPageLocators.ADD_TO_CART_BUTTON
        product_card_page.open()
        assert product_card_page.is_element_present(
            add_to_cart_button
        ), 'Add to cart button is not present on product card page.'

    def test_quantity_input_present(self, browser):
        product_card_page = ProductCardPage(browser)
        quantity_input = ProductCardPageLocators.QUANTITY_INPUT
        product_card_page.open()
        assert product_card_page.is_element_present(
            quantity_input
        ), 'Quantity input is not present on product card page.'

    def test_options_dropdown_present(self, browser):
        product_card_page = ProductCardPage(browser)
        options_dropdown = ProductCardPageLocators.OPTIONS_DROPDOWN
        product_card_page.open()
        assert product_card_page.is_element_present(
            options_dropdown
        ), 'Options dropdown is not present on product card page.'

    def test_grid_button_present(self, browser):
        product_card_page = ProductCardPage(browser)
        description_tab = ProductCardPageLocators.DESCRIPTION_TAB
        product_card_page.open()
        assert product_card_page.is_element_present(
            description_tab
        ), 'Description tab is not present on product card page.'
