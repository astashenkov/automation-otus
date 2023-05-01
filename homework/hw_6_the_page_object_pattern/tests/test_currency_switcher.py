from ..components.currency_switcher import CurrencySwitcher
from ..pages.catalog_page import CatalogPage
from ..pages.main_page import MainPage
from ..pages.product_card_page import ProductCardPage
from ..pages.registration_page import RegistrationPage


class TestCurrencySwitcher:
    def test_currency_switcher_on_main_page(self, driver):
        MainPage(driver).open()
        currency_switcher = CurrencySwitcher(driver)

        currency_switcher.choose_euro()
        assert currency_switcher.selected_currency == 'Euro', 'Selected currency is not Euro'

        currency_switcher.choose_dollar()
        assert currency_switcher.selected_currency == 'Dollar', 'Selected currency is not Dollar'

        currency_switcher.choose_pound()
        assert currency_switcher.selected_currency == 'Pound', 'Selected currency is not Pound'

    def test_currency_switcher_on_product_card_page(self, driver):
        ProductCardPage(driver).open()
        currency_switcher = CurrencySwitcher(driver)

        currency_switcher.choose_euro()
        assert currency_switcher.selected_currency == 'Euro', 'Selected currency is not Euro'

        currency_switcher.choose_dollar()
        assert currency_switcher.selected_currency == 'Dollar', 'Selected currency is not Dollar'

        currency_switcher.choose_pound()
        assert currency_switcher.selected_currency == 'Pound', 'Selected currency is not Pound'

    def test_currency_switcher_on_catalog_page(self, driver):
        CatalogPage(driver).open()
        currency_switcher = CurrencySwitcher(driver)

        currency_switcher.choose_euro()
        assert currency_switcher.selected_currency == 'Euro', 'Selected currency is not Euro'

        currency_switcher.choose_dollar()
        assert currency_switcher.selected_currency == 'Dollar', 'Selected currency is not Dollar'

        currency_switcher.choose_pound()
        assert currency_switcher.selected_currency == 'Pound', 'Selected currency is not Pound'

    def test_currency_switcher_on_registration_page(self, driver):
        RegistrationPage(driver).open()
        currency_switcher = CurrencySwitcher(driver)

        currency_switcher.choose_euro()
        assert currency_switcher.selected_currency == 'Euro', 'Selected currency is not Euro'

        currency_switcher.choose_dollar()
        assert currency_switcher.selected_currency == 'Dollar', 'Selected currency is not Dollar'

        currency_switcher.choose_pound()
        assert currency_switcher.selected_currency == 'Pound', 'Selected currency is not Pound'
