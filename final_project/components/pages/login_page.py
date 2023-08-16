from components.pages.base_page import Page


class LoginPage(Page):

    REL_URL = '/login'

    def __init__(self, driver, rel_url=REL_URL):
        super().__init__(driver=driver, rel_url=rel_url)
