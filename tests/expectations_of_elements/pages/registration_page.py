from .main_page import MainPage


class RegistrationPage(MainPage):
    def __init__(self, driver):
        super().__init__(driver)
        self._url = f'{self._url}index.php?route=account/register'
