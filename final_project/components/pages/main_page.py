import allure

from components.pages.base_page import Page
from helpers.locators import by_css


class MainPage(Page):
    LOCATOR_SLIDER_CAROUSEL = by_css('#slider-carousel')
    LOCATOR_FEATURE_ITEMS = by_css('.features_items')

    def __init__(self, driver, root_url):
        super().__init__(
            driver=driver,
            root_url=root_url,
            rel_url='/',
            page_detect_locator=self.LOCATOR_FEATURE_ITEMS
        )

    @allure.step('Check is carousel slider exist')
    def is_carousel_slider_exist(self):
        try:
            self.custom_find_element(locator=self.LOCATOR_SLIDER_CAROUSEL)
        except TimeoutError:
            return False
        return True
