from urllib.parse import urljoin
from .main_page import MainPage


class ProductCardPage(MainPage):
    def __init__(self, driver):
        super().__init__(driver)
        self._url = urljoin(driver.browser_base_url, '/en-gb/product/tablet/samsung-galaxy-tab-10-1')
