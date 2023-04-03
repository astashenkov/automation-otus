import pytest
import requests


@pytest.mark.ya
def test_request_url_and_check_response_code(url, status_code):
    response = requests.get(url)
    assert response.status_code == status_code, f'Unexpected status code – {response.status_code}.'
