from .main_page import MainPage


class RegistrationPage(MainPage):
    def __init__(self, driver):
        super().__init__(driver)
        self._url = f'{driver.browser_base_url}en-gb?route=account/register'
