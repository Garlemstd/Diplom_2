from allure import step
from utils import authorization_header
from steps.login_steps import AuthSteps
from data.order_data import OrderDataModel
from routes.routes import routes
from settings import base_url
import requests


class OrderSteps:
    def __init__(self):
        self.order_route = routes.GET_ORDERS_NO_AUTH
        self.authorization = AuthSteps().get_user_token
        self.order_data = OrderDataModel().order_data()

    @step('Создание заказа')
    def make_an_order(self, order_data=None, token=None):
        if not order_data:
            order_data = self.order_data
        if not token:
            token = self.authorization()
        headers = authorization_header(token)
        response = requests.post(url=f'{base_url}{self.order_route}', json=order_data, headers=headers)
        return response

    @step('Просмотр заказов пользователя')
    def get_user_orders(self, token=None):
        if not token:
            token = self.authorization()
        headers = authorization_header(token)
        response = requests.get(url=f'{base_url}{self.order_route}', headers=headers)
        return response


