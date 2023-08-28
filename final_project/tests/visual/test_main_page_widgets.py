import pytest

from components.pages.main_page import MainPage
from components.pages.contact_us_page import ContactUsPage


@pytest.mark.main_page
class TestMainPageWidgets:

    def test_carousel_slide_is_exist(self, driver, base_url):
        main_page = MainPage(driver=driver, root_url=base_url)
        main_page.view()

        assert main_page.is_carousel_slider_exist(), 'There is not carousel slider on current page'

    def test_features_items_on_page(self, driver, base_url):
        main_page = MainPage(driver=driver, root_url=base_url)
        main_page.view()

        assert main_page.is_features_items_on_page(), 'There is not the features items on current page'


@pytest.mark.contact_us
class TestContactUs:

    def test_send_subject_to_company(self, driver, base_url):
        contact_us_page = ContactUsPage(driver=driver, root_url=base_url)
        contact_us_page.view()
        contact_us_page.fill_and_send_data()

        assert contact_us_page.is_details_submitted(), "Details weren't success submitted."

    def test_contact_info_is_exist(self, driver, base_url):
        contact_us_page = ContactUsPage(driver=driver, root_url=base_url)
        contact_us_page.view()

        assert contact_us_page.is_contact_info_present(), "Contact info didn't present."
