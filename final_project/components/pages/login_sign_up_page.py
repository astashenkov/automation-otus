from components.pages.base_page import Page
from helpers.locators import by_css


class LoginSignUpPage(Page):
    LOCATOR_LOGIN_FORM = by_css('.login-form')
    LOCATOR_LOGIN_EMAIL = by_css('[data-qa="login-email"]')
    LOCATOR_LOGIN_PASSWORD = by_css('[data-qa="login-password"]')
    LOCATOR_LOGIN_BUTTON = by_css('[data-qa="login-button"]')
    LOCATOR_SIGNUP_NAME = by_css('[data-qa="signup-name"]')
    LOCATOR_SIGNUP_EMAIL = by_css('[data-qa="signup-email"]')
    LOCATOR_SIGNUP_BUTTON = by_css('[data-qa="signup-button"]')

    def __init__(self, driver, root_url):
        super().__init__(
            driver=driver,
            root_url=root_url,
            rel_url='/login',
            page_detect_locator=self.LOCATOR_LOGIN_FORM
        )

    def fill_login_email_input(self, text: str = 'test@gmail.com'):
        login_email_input = self.custom_find_element(locator=self.LOCATOR_LOGIN_EMAIL)
        login_email_input.send_keys(text)

    def fill_login_password_input(self, text: str = '123tesT'):
        login_password_input = self.custom_find_element(locator=self.LOCATOR_LOGIN_PASSWORD)
        login_password_input.send_keys(text)

    def click_login_button(self):
        login_button = self.custom_find_element(locator=self.LOCATOR_LOGIN_BUTTON)
        login_button.click()

    def fill_signup_name_input(self, text: str = 'tester'):
        signup_name_input = self.custom_find_element(locator=self.LOCATOR_SIGNUP_NAME)
        signup_name_input.send_keys(text)

    def fill_signup_email_input(self, text: str = 'test@gmail.com'):
        signup_email_input = self.custom_find_element(locator=self.LOCATOR_SIGNUP_EMAIL)
        signup_email_input.send_keys(text)

    def click_signup_button(self):
        signup_button = self.custom_find_element(locator=self.LOCATOR_SIGNUP_BUTTON)
        signup_button.click()
