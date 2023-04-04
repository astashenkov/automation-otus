import pytest
import requests
import cerberus


class TestDogCeo:
    URL = 'https://dog.ceo/api/'

    @pytest.mark.dog_ceo
    @pytest.mark.parametrize('quantity_dogs', [i for i in range(1, 51)])
    def test_request_random_quantity_of_dogs(self, quantity_dogs):
        response = requests.get(f'{self.URL}breeds/image/random/{quantity_dogs}')
        schema = {
            'message': {'type': 'list'},
            'status': {'type': 'string'}
        }
        schema_validator = cerberus.Validator(schema)

        assert response.status_code == 200, f'Request is failed with status {response.status_code}.'
        assert schema_validator(response.json()), f'Incorrect JSON response schema when use {quantity_dogs} dog(s).'
        assert len(response.json()['message']) == quantity_dogs, \
            f'Quantity of received dogs is not equal to {quantity_dogs}.'

    @pytest.mark.dog_ceo
    def test_receive_all_dog_images(self):
        response = requests.get(f'{self.URL}breed/hound/images')
        schema = {
            'message': {'type': 'list'},
            'status': {'type': 'string'}
        }
        schema_validator = cerberus.Validator(schema)

        assert response.status_code == 200, f'Request is failed with status {response.status_code}.'
        assert schema_validator(response.json()), 'Incorrect JSON response schema.'
        assert response.json()['message'], 'Error! Received an empty array of images.'

    @pytest.mark.dog_ceo
    @pytest.mark.parametrize('sub_breed', requests.get(f'{URL}breed/hound/list').json()['message'])
    def test_receive_dogs_of_each_sub_breed(self, sub_breed):
        response = requests.get(f'{self.URL}breed/hound/{sub_breed}/images')
        schema = {
            'message': {'type': 'list'},
            'status': {'type': 'string'}
        }
        schema_validator = cerberus.Validator(schema)

        assert response.status_code == 200, f'Request is failed with status {response.status_code}.'
        assert schema_validator(response.json()), 'Incorrect JSON response schema.'
        assert response.json()['message'], f'Dogs of the {sub_breed} sub_breed are not received.'

    @pytest.mark.dog_ceo
    def test_receive_all_breeds_list(self):
        response = requests.get(f'{self.URL}breeds/list/all')
        schema = {
            'message': {'type': 'dict'},
            'status': {'type': 'string'}
        }
        schema_validator = cerberus.Validator(schema)

        assert response.status_code == 200, f'Request is failed with status {response.status_code}.'
        assert schema_validator(response.json()), 'Incorrect JSON response schema.'
        assert response.json()['message'], 'Received an empty array of breeds.'

    @pytest.mark.dog_ceo
    @pytest.mark.parametrize('sub_breed, quantity_dogs, expected_code',
                             [
                                 ('rabbit', 0, 404),
                                 ('english', 15, 200),
                                 ('crocodile', 0, 404),
                                 ('basset', 10, 200),
                                 ('penguin', 0, 404)
                             ])
    def test_multiple_images_from_sub_breed_collection(self, sub_breed, expected_code, quantity_dogs):
        response = requests.get(f'{self.URL}breed/hound/{sub_breed}/images/random/{quantity_dogs}')
        schema = {
            'code': {'type': 'integer'},
            'message': {'type': ['list', 'string']},
            'status': {'type': 'string'}
        }
        schema_validator = cerberus.Validator(schema)

        assert response.status_code == expected_code, f'Unexpected code – {response.status_code}.'
        assert schema_validator(response.json()), 'Incorrect JSON response schema.'
