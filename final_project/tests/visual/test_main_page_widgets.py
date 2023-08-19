from components.pages.main_page import MainPage


class TestMainPageWidgets:

    def test_carousel_slide_is_exist(self, driver, base_url):
        main_page = MainPage(driver=driver, root_url=base_url)
        main_page.view()

        assert main_page.is_carousel_slider_exist(), 'There is not carousel slider on current page'
