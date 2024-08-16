from allure import step
from utils import authorization_header
from steps.login_steps import AuthSteps
from data.order_data import OrderDataModel
from routes.routes import Routes
import requests


class OrderSteps:
    def __init__(self):
        self.order_route = Routes().GET_ORDERS_NO_AUTH
        self.order_data = OrderDataModel().order_data()

    @step('Создание заказа')
    def make_an_order(self, order_data=None, token=None):
        if not order_data:
            order_data = self.order_data
        if not token:
            token = AuthSteps().get_user_token()
        headers = authorization_header(token)
        response = requests.post(url=f'{Routes().BASE_URL}{self.order_route}', json=order_data, headers=headers)
        return response

    @step('Просмотр заказов пользователя')
    def get_user_orders(self, token=None):
        if not token:
            token = AuthSteps().get_user_token
        headers = authorization_header(token)
        response = requests.get(url=f'{Routes().BASE_URL}{self.order_route}', headers=headers)
        return response


