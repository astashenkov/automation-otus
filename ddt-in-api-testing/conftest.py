import pytest


def pytest_addoption(parser):
    parser.addoption(
        '--url',
        default='https://ya.ru',
        action='store',
        help='select URL for test'
    )
    parser.addoption(
        '--status_code',
        default=200,
        action='store',
        help='select status code for test'
    )


@pytest.fixture(scope="function")
def url(request):
    return request.config.getoption('--url')


@pytest.fixture(scope="function")
def status_code(request):
    return int(request.config.getoption('--status_code'))
