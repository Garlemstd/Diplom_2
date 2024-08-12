from data.user_data import UserRegistrationModel
import allure


@allure.suite('Тесты на авторизацию пользователя')
class TestLogin:

    @allure.title("Авторизация от лица тестового пользователя")
    def test_user_authorization(self, login_steps, create_and_delete_user_for_test):
        user_authorization = login_steps.authorize_user()
        assert user_authorization.ok

    @allure.title("Авторизация от лица несуществующего пользователя")
    def test_non_existing_user_authorization(self, login_steps, prepare_random_user, exceptions):
        invalid_authorization = login_steps.authorize_user(prepare_random_user)
        assert invalid_authorization.status_code == 401
        assert invalid_authorization.json()['message'] == exceptions.incorrect_credentials

    @allure.title("Редактирование тестового пользователя с авторизационным токеном")
    def test_edit_user_with_authorization_token(self, login_steps, user_steps, create_and_delete_user_for_test):
        user_authorization = login_steps.authorize_user()
        assert user_authorization.ok
        update_user = user_steps.update_user(user=UserRegistrationModel().dict())
        assert update_user.ok

    @allure.title("Редактирование тестового пользователя без авторизационного токена")
    def test_edit_user_without_authorization_token(self, login_steps, user_steps, exceptions):
        update_user = user_steps.update_user(token='fake_token')
        assert update_user.status_code == 401
        assert update_user.json()['message'] == exceptions.not_authorized
