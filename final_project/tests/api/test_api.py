import pytest

import cerberus
import requests


@pytest.mark.api
class TestApi:
    PRODUCTS_LIST_URL = 'https://automationexercise.com/api/productsList'
    USER_DETAIL_URL = 'https://automationexercise.com/api/getUserDetailByEmail'

    SCHEMA_RESPONSE = {
        'responseCode': {'type': 'integer'},
        'message': {'type': 'string'}
    }

    USER_SCHEMA = {
        'responseCode': {'type': 'integer'},
        'user': {'type': 'dict'}
    }

    def test_get_products_list(self):
        response = requests.get(url=self.PRODUCTS_LIST_URL)

        assert response.status_code == 200, f'Request is failed with status {response.status_code}.'
        assert len(response.json()['products']) > 0, 'Empty products fild received.'

    def test_post_products_list(self):
        response = requests.post(url=self.PRODUCTS_LIST_URL)
        schema_validator = cerberus.Validator(self.SCHEMA_RESPONSE)

        assert response.status_code == 200, f'Request is failed with status {response.status_code}.'
        assert schema_validator(response.json()), f'Wrong JSON response schema: {schema_validator.errors}.'
        assert response.json()['message'], 'This request method is not supported.'

    def test_get_user_detail(self):
        response = requests.get(url=self.USER_DETAIL_URL, params={'email': 'test@test.com'})
        schema_validator = cerberus.Validator(self.USER_SCHEMA)
        print(response.json())

        assert response.status_code == 200, f'Request is failed with status {response.status_code}.'
        assert schema_validator(response.json()), f'Wrong JSON response schema: {schema_validator.errors}.'
        assert response.json()['user']['email'] == 'test@test.com', 'Wrong user received.'

    @pytest.mark.parametrize('status_code', [
        (404, False),
        (200, True),
        (500, False),
        (301, False),
        (302, False)
    ])
    def test_multiple_images_from_sub_breed_collection(self, status_code):
        response = requests.get(self.PRODUCTS_LIST_URL)
        checking_code = response.status_code == status_code[0]

        assert checking_code == status_code[1], f'Unexpected code – {response.status_code}.'
