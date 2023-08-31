import cerberus
import pytest
import requests


@pytest.mark.placeholder
class TestPlaceHolder:
    URL = 'https://jsonplaceholder.typicode.com/'
    SCHEMA = {
        'id': {'type': 'integer'},
        'title': {'type': 'string'},
        'body': {'type': 'string'},
        'userId': {'type': 'integer'}
    }

    @pytest.mark.parametrize('route, expected_code', [
        ('posts/19/comments', 200),
        ('albums/32/photos', 200),
        ('wrong/123', 404),
        ('users/10/albums', 200),
        ('posts/123/fail', 404),
        ('users/3/todos', 200),
        ('users/2/posts', 200)
    ])
    def test_get_content_from_different_routes(self, route, expected_code):
        response = requests.get(f'{self.URL}{route}')
        assert response.status_code == expected_code, f'Wrong status code – {response.status_code}.'

    def test_create_user_post(self, user_post):
        response = requests.post(f'{self.URL}posts', json=user_post)
        schema_validator = cerberus.Validator(self.SCHEMA)

        assert response.status_code == 201, "Can't create user post."
        assert schema_validator(response.json()), f'Wrong schema validation {schema_validator.errors}.'

    def test_replace_user_post(self, user_post):
        response = requests.put(f'{self.URL}posts/1', json=user_post)
        schema_validator = cerberus.Validator(self.SCHEMA)

        assert response.status_code == 200, f'Request is fail with {response.status_code} code.'
        assert schema_validator(response.json()), f'Wrong schema validation {schema_validator.errors}.'

    def test_update_title_of_user_post(self):
        new_title = {
            'title': 'Title from test',
        }
        response = requests.patch(f'{self.URL}posts/1', params=new_title)
        assert response.status_code == 200, f'Request is fail with {response.status_code} code.'

    @pytest.mark.parametrize('post_id', [i for i in range(0, 11)])
    def test_delete_user_posts(self, post_id):
        response = requests.delete(f'{self.URL}posts/{post_id}')
        assert response.status_code == 200, f"Can't delete post (id={post_id})."
