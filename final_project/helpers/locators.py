from typing import Tuple
from selenium.webdriver.common.by import By

Locator = Tuple[str, str]


def by_css(*selector: str) -> Locator:
    return By.CSS_SELECTOR, ','.join(selector)


def by_xpath(selector: str) -> Locator:
    return By.XPATH, selector


def by_name(element_name: str) -> Locator:
    return by_css(f'[name="{element_name}"]')
