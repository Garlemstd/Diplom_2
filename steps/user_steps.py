from data.user_data import UserRegistrationModel
from steps.login_steps import AuthSteps
from allure import step
from utils import authorization_header
from routes.routes import Routes
import requests


class UserSteps:
    def __init__(self):
        self.route_register_user = Routes().REGISTER_USER
        self.route_delete_user = Routes().DELETE_USER
        self.register_model = UserRegistrationModel()

    @step('Запрос токена у сервера')
    def get_token(self):
        response = AuthSteps().authorize_user()
        get_token_from_response = response.json()["accessToken"]
        return get_token_from_response

    @step('Регистрация пользователя')
    def register_user(self, user=None):
        if not user:
            user = self.register_model.dict()
        response = requests.post(url=f'{Routes().BASE_URL}{self.route_register_user}', json=user)
        return response

    @step('Удаление пользователя')
    def delete_user(self, token=None):
        if not token:
            token = self.get_token()
        headers = authorization_header(token)
        response = requests.delete(url=f'{Routes().BASE_URL}{self.route_delete_user}', headers=headers)
        return response

    @step('Обновление данных пользователя')
    def update_user(self, user=None, token=None):
        if not user:
            user = self.register_model.dict()
        if not token:
            token = self.get_token()
        headers = authorization_header(token)
        response = requests.patch(url=f'{Routes().BASE_URL}{self.route_delete_user}', json=user, headers=headers)
        return response

