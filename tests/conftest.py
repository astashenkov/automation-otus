import pytest


@pytest.fixture(autouse=True)
def first():
    print('\nFirst')


@pytest.fixture(autouse=True)
def fourth():
    print('\nFourth')
