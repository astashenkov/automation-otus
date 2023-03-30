import pytest
import requests


@pytest.mark.parametrize('quantity_dogs', [i for i in range(1, 51)])
def test_request_random_quantity_of_dogs(quantity_dogs):
    response = requests.get(f'https://dog.ceo/api/breeds/image/random/{quantity_dogs}')
    assert response.json()['status'] == 'success', f'Request is failed with status {response.status_code}.'
    assert len(response.json()['message']) == quantity_dogs, \
        f'Quantity of received dogs is not equal to {quantity_dogs}.'


def test_receive_all_dog_images():
    response = requests.get('https://dog.ceo/api/breed/hound/images')
    assert response.json()['status'] == 'success', f'Request is failed with status {response.status_code}.'
    assert response.json()['message'], 'Received an empty array of images.'


@pytest.mark.parametrize('sub_breed', requests.get('https://dog.ceo/api/breed/hound/list').json()['message'])
def test_receive_dogs_of_each_sub_breed(sub_breed):
    response = requests.get(f'https://dog.ceo/api/breed/hound/{sub_breed}/images')
    assert response.json()['status'] == 'success', f'Request is failed with status {response.status_code}.'
    assert response.json()['message'], f'Dogs of the {sub_breed} sub_breed are not received.'


def test_receive_all_breeds_list():
    response = requests.get('https://dog.ceo/api/breeds/list/all')
    assert response.json()['status'] == 'success', f'Request is failed with status {response.status_code}.'
    assert response.json()['message'], f'Received an empty array of breeds.'


@pytest.mark.parametrize('quantity_dogs', [i for i in range(1, 4)])
@pytest.mark.parametrize('breed', requests.get('https://dog.ceo/api/breeds/list/all').json()['message'])
def test_multiple_images_from_breed_collection(quantity_dogs, breed):
    response = requests.get(f'https://dog.ceo/api/breed/{breed}/images/random/{quantity_dogs}')
    assert response.json()['status'] == 'success', f'Request is failed with status {response.status_code}.'
    assert response.json()['message'], f'Dogs of the {breed} breed are not received.'
    if len(requests.get(f'https://dog.ceo/api/breed/{breed}/images/').json()['message']) > 2:
        assert len(response.json()['message']) == quantity_dogs, \
            f'Quantity of received dogs is not equal to {quantity_dogs}.'
