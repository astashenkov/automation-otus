import pytest


@pytest.fixture(autouse=True)
def second():
    print('\nSecond')


@pytest.fixture(autouse=True)
def third():
    print('\nThird')


@pytest.fixture(autouse=True)
def fifth():
    print('\nFifth')


@pytest.mark.parametrize('val', [1, 2, 3, 4, 5])
def test_example(val):
    assert val == 3
