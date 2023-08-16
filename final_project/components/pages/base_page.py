from typing import Optional

import allure

from helpers.locators import by_css
from helpers.locators import Locator
from helpers.driver_helpers import DriverHelpers


class Page:
    LOCATOR_MAIN_MENU = by_css('.shop-menu')
    LOCATOR_MAIN_LOGO = by_css('.logo')

    def __init__(
            self,
            driver,
            rel_url: str = '',
            full_url: str | None = '',
            page_detect_locator: Optional['Locator'] = None,
    ):

        self.driver = driver
        self.rel_url = rel_url
        self._full_url = full_url
        self._page_detect_locator = page_detect_locator

    @property
    def full_url(self) -> str:
        if not self.rel_url and not self._full_url:
            raise AttributeError('Need specify rel_url or full_url')

        full_url = self._full_url

        if not full_url:
            full_url = f'{self.root_url}{self.rel_url}'

        if self._url_parameters:
            is_param_exist = len(full_url.split('&')) > 1
            full_url = f'{full_url}?{self._url_parameters}'
            if is_param_exist:
                full_url = f'{full_url}&{self._url_parameters}'

        return full_url

    @full_url.setter
    def full_url(self, url: str):
        self._full_url = url

    @property
    def is_current_url(self) -> bool:
        return self.driver.current_url == self.full_url

    @property
    def page_detect_locator(self) -> 'Locator':
        if self._page_detect_locator:
            return self._page_detect_locator
        raise Exception('Need specified page_detect_locator Page class argument')

    @property
    def is_current_page(self) -> bool:
        return self.driver.element_is_exist(self.page_detect_locator)

    def view(self) -> None:
        with allure.step(f'Navigate to {self.full_url}'):
            self.driver.get(self.full_url)
