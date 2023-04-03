import pytest


class TestOpenBreweryDB:
    URL = 'https://www.openbrewerydb.org/'

    @pytest.mark.open_brewery_db
    def test_first(self):
        pass

    @pytest.mark.open_brewery_db
    def test_second(self):
        pass

    @pytest.mark.open_brewery_db
    def test_third(self):
        pass

    @pytest.mark.open_brewery_db
    def test_fourth(self):
        pass

    @pytest.mark.open_brewery_db
    def test_fifth(self):
        pass
