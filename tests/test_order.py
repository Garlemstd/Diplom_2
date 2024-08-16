from data.user_data import UserRegistrationModel
import allure
from server_exceptions.exceptions_text import ExceptionsText
from data.order_data import OrderDataModel


@allure.suite('Тесты на работу с заказами')
class TestOrder:

    @allure.title("Создание заказа с авторизацией")
    def test_make_an_order_with_authorization(self, order_steps, assertions, create_and_delete_user_for_test):
        make_an_order = order_steps.make_an_order()
        assert make_an_order.ok
        assert make_an_order.json()['order']['owner']['name'] == UserRegistrationModel().dict()['name']

    @allure.title("Создание заказа без авторизации")
    def test_make_an_order_without_authorization(self, order_steps):
        make_an_order_without_token = order_steps.make_an_order(token='fake_token')
        assert make_an_order_without_token.ok
        assert make_an_order_without_token.json()['success'] is True

    @allure.title("Создание заказа с ингредиентами")
    def test_make_an_order_with_ingredients(self, order_steps, create_and_delete_user_for_test):
        make_an_order_with_ingredients = order_steps.make_an_order()
        assert make_an_order_with_ingredients.ok
        assert OrderDataModel().fluorescent_bread_r2_d3 in make_an_order_with_ingredients.text

    @allure.title("Создание заказа без ингредиентов")
    def test_make_an_order_without_ingredients(self, order_steps, create_and_delete_user_for_test):
        make_an_order_without_ingredients = order_steps.make_an_order(order_data=OrderDataModel().empty_ingredients_data())
        assert make_an_order_without_ingredients.status_code == 400
        assert make_an_order_without_ingredients.json()['message'] == ExceptionsText().no_ingredients_order

    @allure.title("Создание заказа с несуществующим ID ингредиента")
    def test_make_an_order_with_fake_ingredient_id(self, order_steps, create_and_delete_user_for_test):
        make_order_with_fake_ingredient_id = order_steps.make_an_order(order_data=OrderDataModel().fake_ingredients_data())
        assert make_order_with_fake_ingredient_id.status_code == 500

    @allure.title("Получение собственных заказов с авторизацией")
    def test_get_user_orders_with_authorization(self, order_steps, assertions, create_and_delete_user_for_test):
        make_an_order_to_check = order_steps.make_an_order()
        assert make_an_order_to_check.ok
        get_orders = order_steps.get_user_orders()
        assertions.created_id_equal_requested_id(make_an_order_to_check, get_orders)
        assert get_orders.ok

    @allure.title("Получение собственных заказов  без авторизации")
    def test_get_user_orders_without_authorization(self, order_steps,):
        get_orders_without_token = order_steps.get_user_orders(token='fake_token')
        assert get_orders_without_token.status_code == 401
        assert get_orders_without_token.json()['message'] == ExceptionsText().not_authorized
