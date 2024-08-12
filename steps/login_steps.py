from data.user_data import UserRegistrationModel
from allure import step
from routes.routes import routes
import requests
from settings import base_url


class AuthSteps:
    def __init__(self):
        self._login_endpoint = routes.LOGIN_USER

    @step('Авторизация пользователя')
    def authorize_user(self, user: dict = None):
        if user is None:
            user = UserRegistrationModel().dict()
        response = requests.post(url=f'{base_url}{self._login_endpoint}', json=user)
        return response

    @step('Получение токена пользователя из ответа')
    def get_user_token(self, user: dict = None):
        response = self.authorize_user(user)
        return response.json().get('accessToken')
