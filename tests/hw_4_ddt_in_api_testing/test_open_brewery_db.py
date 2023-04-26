import cerberus
import pytest
import requests


@pytest.mark.open_brewery_db
class TestOpenBreweryDB:
    URL = 'https://api.openbrewerydb.org/v1/breweries/'

    def test_get_all_breweries(self):
        response = requests.get(self.URL)
        assert response.status_code == 200, f'Request is fail with {response.status_code} code.'

    @pytest.mark.parametrize('query, city', [
        ('san_diego', 'San Diego'),
        ('new_york', 'New York'),
        ('chicago', 'Chicago')
    ])
    def test_random_brewery_by_city(self, query, city):
        response = requests.get(f'{self.URL}?by_city={query}')

        assert response.status_code == 200, f'Request is fail with {response.status_code} code.'
        assert response.json()[0]["city"] == city, f'Wrong city in the response – {response.json()[0]["city"]}'

    @pytest.mark.parametrize('size, expected_size', [
        (50, 50),
        (51, 50),
        (35, 35),
        (25, 25),
        (7, 7),
        (0, 1),
        (1, 1)
    ])
    def test_random_brewery(self, size, expected_size):
        response = requests.get(f'{self.URL}random?size={size}')

        assert response.status_code == 200, f'Request is fail with {response.status_code} code.'
        assert len(response.json()) == expected_size, f'Unexpected size of breweries – {len(response.json())}.'

    @pytest.mark.parametrize('word, quantity, expected_quantity', [
        ('dog', 5, 5),
        ('kiwi', 10, 0),
        ('cat', 3, 3),
        ('tomatoes', 20, 0),
        ('penguin', 1, 0)
    ])
    def test_search_breweries(self, word, quantity, expected_quantity):
        response = requests.get(f'{self.URL}search?query={word}&per_page={quantity}')

        assert response.status_code == 200, f'Request is fail with {response.status_code} code.'
        assert len(response.json()) == expected_quantity, 'Unexpected quantity of breweries.'

    @pytest.mark.parametrize('parameter', [
        '',
        '?by_country=south_korea',
        '?by_type=micro',
        '?by_country=us'
    ])
    def test_metadata(self, parameter):
        response = requests.get(f'{self.URL}meta{parameter}')
        schema = {
            'total': {'type': 'string'},
            'page': {'type': 'string'},
            'per_page': {'type': 'string'}
        }
        schema_validator = cerberus.Validator(schema)

        assert response.status_code == 200, f'Request is fail with {response.status_code} code.'
        assert schema_validator(response.json()), f'Wrong schema validation {schema_validator.errors}.'
