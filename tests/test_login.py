import allure
from server_exceptions.exceptions_text import ExceptionsText
from data.user_data import UserRegistrationModel


@allure.suite('Тесты на авторизацию пользователя')
class TestLogin:

    @allure.title("Авторизация от лица тестового пользователя")
    def test_user_authorization(self, login_steps, create_and_delete_user_for_test):
        user_authorization = login_steps.authorize_user()
        assert user_authorization.ok
        assert "accessToken" in user_authorization.text

    @allure.title("Авторизация от лица несуществующего пользователя")
    def test_non_existing_user_authorization(self, login_steps, prepare_test_user):
        invalid_authorization = login_steps.authorize_user(prepare_test_user)
        assert invalid_authorization.status_code == 401
        assert invalid_authorization.json()['message'] == ExceptionsText().incorrect_credentials

    @allure.title("Редактирование тестового пользователя с авторизационным токеном")
    def test_edit_user_with_authorization_token(self, login_steps, user_steps, create_and_delete_user_for_test,
                                                prepare_test_user):
        user_authorization = login_steps.authorize_user()
        assert user_authorization.ok
        assert user_authorization.json()['user']['email'] == UserRegistrationModel().email
        update_user = user_steps.update_user(user=UserRegistrationModel().dict())
        assert update_user.ok
        assert update_user.json()['success'] is True

    @allure.title("Редактирование тестового пользователя без авторизационного токена")
    def test_edit_user_without_authorization_token(self, login_steps, user_steps):
        update_user = user_steps.update_user(token='fake_token')
        assert update_user.status_code == 401
        assert update_user.json()['message'] == ExceptionsText().not_authorized
