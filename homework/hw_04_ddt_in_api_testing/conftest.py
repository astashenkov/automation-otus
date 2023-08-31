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


@pytest.fixture()
def url(request) -> str:
    return request.config.getoption('--url')


@pytest.fixture()
def status_code(request) -> int:
    return int(request.config.getoption('--status_code'))


@pytest.fixture()
def user_post() -> dict:
    return {
        'id': 42,
        'title': 'Test user post title',
        'body': 'Test user post body',
        'userId': 42
    }
