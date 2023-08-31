import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import urljoin


class MainPage:

    def __init__(self, driver):
        self._driver = driver
        self._url = urljoin(driver.browser_base_url, '/en-gb?route=common/home')

    @allure.step('Opeen page')
    def open(self) -> None:
        self._driver.get(self._url)
        allure.attach(
            name='Attach_with_HTML_type',
            body=self._driver.page_source,
            attachment_type=allure.attachment_type.HTML
        )

    @allure.step('Checking for an element on the page')
    def is_element_present(self, element: tuple) -> bool:
        try:
            WebDriverWait(self._driver, 2).until(EC.presence_of_element_located(element))
            return True
        except TimeoutException:
            allure.attach(
                name=f'{self._driver.current_url}'[:90],
                body=self._driver.get_screenshot_as_png(),
                attachment_type=allure.attachment_type.PNG
            )
            return False
