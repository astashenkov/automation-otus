from .main_page import MainPage


class ProductCardPage(MainPage):
    def __init__(self, driver):
        super().__init__(driver)
        self._url = f'{driver.browser_base_url}en-gb/product/canon-eos-5d?path=33'
