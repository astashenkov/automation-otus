import allure
import pytest

from ..pages.registration_page import RegistrationPage


@allure.title('Регистрация нового пользователя')
@pytest.mark.register_new_user
@pytest.mark.parametrize('user', [
    ('Guido', 'van Rossum', 'gvanrossum@python.com', 'gvanrossum'),
    ('Joe', 'Rogan', 'joerogan@python.com', 'joerogan'),
    ('James', 'Hetfield', 'jameshetfield@python.com', 'jameshetfield'),
    ('Frank', 'Ocean', 'frankocean@python.com', 'frankocean'),
    ('Clint', 'Eastwood', 'clinteastwood@python.com', 'clinteastwood')
])
def test_register_new_user(driver, user):
    registration_page = RegistrationPage(driver)
    registration_page.open()
    registration_page.fill_out_the_required_registration_data(*user)
    registration_page.activate_privacy_policy_checkbox()
    registration_page.click_submit_button()
    assert registration_page.is_success_created_account(), 'An account was not created'
