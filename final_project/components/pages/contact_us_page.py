import allure

from components.pages.base_page import Page
from helpers.locators import by_css


class ContactUsPage(Page):
    LOCATOR_CONTACT_FORM = by_css('.contact-form')
    LOCATOR_INPUT_NAME = by_css('[data-qa="name"]')
    LOCATOR_INPUT_EMAIL = by_css('[data-qa="email"]')
    LOCATOR_INPUT_SUBJECT = by_css('[data-qa="subject"]')
    LOCATOR_INPUT_MESSAGE = by_css('[data-qa="message"]')
    LOCATOR_SUBMIT_BUTTON = by_css('[data-qa="submit-button"]')
    LOCATOR_SUCCESS_ALERT = by_css('.alert-success')
    LOCATOR_CONTACT_INFO = by_css('.contact-info')

    def __init__(self, driver, root_url):
        super().__init__(
            driver=driver,
            root_url=root_url,
            rel_url='/contact_us',
            page_detect_locator=self.LOCATOR_CONTACT_FORM
        )

    @allure.step('Fill inputs')
    def fill_and_send_data(self):
        name_input = self.custom_find_element(locator=self.LOCATOR_INPUT_NAME)
        name_input.send_keys('Tester')
        email_input = self.custom_find_element(locator=self.LOCATOR_INPUT_EMAIL)
        email_input.send_keys('tester@gmail.com')
        subject_input = self.custom_find_element(locator=self.LOCATOR_INPUT_SUBJECT)
        subject_input.send_keys('Testing contact us form')
        message_input = self.custom_find_element(locator=self.LOCATOR_INPUT_MESSAGE)
        message_input.send_keys('Test message')
        submit_button = self.custom_find_element(locator=self.LOCATOR_SUBMIT_BUTTON)
        submit_button.click()
        self.driver.switch_to.alert.accept()

    @allure.step('Fill inputs')
    def is_details_submitted(self):
        try:
            self.custom_find_element(locator=self.LOCATOR_SUCCESS_ALERT)
        except TimeoutError:
            return False
        return True

    @allure.step('Fill inputs')
    def is_contact_info_present(self):
        try:
            self.custom_find_element(locator=self.LOCATOR_CONTACT_INFO)
        except TimeoutError:
            return False
        return True
