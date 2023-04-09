import time


class TestOpenCart:
    def test_mock_open_browser(self, browser):
        browser.get('https://www.google.com')
        time.sleep(3)
