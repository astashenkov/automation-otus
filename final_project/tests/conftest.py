import pytest
import allure
import json

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.safari.options import Options as SafariOptions


def pytest_addoption(parser):
    parser.addoption(
        '--browser',
        default='firefox',
        help='Choose browser: Chrome, FireFox, Safari or Edge'
    )
    parser.addoption(
        '--url',
        default='https://www.automationexercise.com',
        help='Choose base URL'
    )
    parser.addoption(
        "--headless",
        action='store_true',
        help='Selecting the browser working mode'
    )


@pytest.fixture()
def driver(request):
    browser_name = request.config.getoption('--browser')
    headless = request.config.getoption('--headless')

    service = Service()

    if browser_name == 'chrome':
        options = ChromeOptions()
        if headless:
            options.add_argument('-headless')
        driver = webdriver.Chrome(service=service, options=options)
    elif browser_name == 'firefox':
        options = FirefoxOptions()
        if headless:
            options.add_argument('-headless')
        driver = webdriver.Firefox(service=service, options=options)
    elif browser_name == 'safari':
        options = SafariOptions()
        if headless:
            options.add_argument('-headless')
        driver = webdriver.Safari(service=service, options=options)
    elif browser_name == 'edge':
        options = EdgeOptions()
        if headless:
            options.add_argument('-headless')
        driver = webdriver.Edge(service=service, options=options)
    else:
        raise ValueError(f'Unsupported browser: {browser_name}')

    driver.maximize_window()

    allure.attach(
        name=driver.session_id,
        body=json.dumps(driver.capabilities, indent=2, ensure_ascii=False),
        attachment_type=allure.attachment_type.JSON
    )

    yield driver

    driver.quit()


@pytest.fixture()
def base_url(request) -> str:
    return request.config.getoption("--url")
