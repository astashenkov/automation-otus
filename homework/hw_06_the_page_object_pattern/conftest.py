import json

import allure
import pytest

from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager


def pytest_addoption(parser):
    parser.addoption(
        '--browser',
        default='firefox',
        help='Choose browser: Chrome, FireFox, Safari, Opera or Edge.'
    )
    parser.addoption(
        '--url',
        default='http://localhost/',
        help='Choose base URL'
    )


@pytest.fixture()
def driver(request):
    browser_name = request.config.getoption('browser').lower()

    if browser_name == 'chrome':
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser_name == 'firefox':
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser_name == 'safari':
        driver = webdriver.Safari()
    elif browser_name == 'opera':
        webdriver_service = service.Service(OperaDriverManager().install())
        webdriver_service.start()

        options = webdriver.ChromeOptions()
        options.add_experimental_option('w3c', True)

        driver = webdriver.Remote(webdriver_service.service_url, options=options)
    elif browser_name == 'edge':
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    else:
        raise ValueError(f'Unsupported browser: {browser_name}')

    driver.browser_base_url = request.config.getoption('url')
    driver.maximize_window()

    allure.attach(
        name=driver.session_id,
        body=json.dumps(driver.capabilities, indent=2, ensure_ascii=False),
        attachment_type=allure.attachment_type.JSON
    )

    yield driver

    driver.quit()
