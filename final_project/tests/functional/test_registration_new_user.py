from components.pages.login_sign_up_page import LoginSignUpPage


class TestLoginAndSignUp:

    def test_user_signup(self, driver, base_url):
        signup_page = LoginSignUpPage(driver=driver, root_url=base_url)
        signup_page.view()

        assert signup_page.is_current_page, f'{signup_page.full_url} is not Sign Up page.'

        signup_page.fill_signup_name_input()
        signup_page.fill_signup_email_input()
        signup_page.click_signup_button()

    # ToDo: Понять как создавать и удалять тестового юзера. Добавить проверку регистрации

    def test_user_login(self, driver, base_url):
        login_page = LoginSignUpPage(driver=driver, root_url=base_url)
        login_page.view()

        assert login_page.is_current_page, f'{login_page.full_url} is not Login page.'

        login_page.fill_login_email_input()
        login_page.fill_login_password_input()
        login_page.click_login_button()

    # ToDo: Понять как создавать и удалять тестового юзера. Добавить проверку логина
