import allure
import pytest
import requests
import variables
import random


class TestTakeOrder:

    @allure.title('Запрос PUT "Принять заказ" для заказа с корректным id')
    def test_take_order_valid_data_receive_ok_status(self, sign_up_new_courier, log_in_courier,
                                                     delete_courier, get_order):
        courier_id = log_in_courier.json()['id']
        order_id = get_order.json()['order']['id']
        with allure.step(f'Отправка запроса PUT: Принятие заказа с id "{order_id}", id курьера "{courier_id}", '
                         f'ожидается сообщение: "ok: true" с кодом "200"'):
            response_take_order = requests.put(f'{variables.TAKE_ORDER}/{order_id}?courierId={courier_id}')
        assert response_take_order.status_code == 200 and response_take_order.json()['ok'] is True

    @allure.title('Запрос PUT "Принять заказ" для заказа с некорректным курьером')
    @pytest.mark.parametrize('courier_id, error_code, error_message', [['', 400, variables.order_empty_data],
                                                                       [random.randrange(1111111, 9999999),
                                                                       404, variables.order_no_such_courier]])
    def test_take_order_invalid_courier_id_error_invalid_data(self, get_order, courier_id,
                                                              error_message, error_code):
        order_id = get_order.json()['order']['id']
        with allure.step(f'Отправка запроса PUT: Принятие заказа с id "{order_id}", id курьера "{courier_id}", '
                         f'ожидается сообщение: "{error_message}" с кодом "{error_code}"'):
            response_take_order = requests.put(f'{variables.TAKE_ORDER}/{order_id}?courierId={courier_id}')
            get_error_message = response_take_order.json()['message']
        assert response_take_order.status_code == error_code and get_error_message == error_message

    @allure.title('Запрос PUT "Принять заказ" для заказа с некорректным id заказа')
    @pytest.mark.parametrize('order_id, error_code, error_message', [['', 400, variables.order_empty_data],
                                                                     [random.randrange(1111111, 9999999),
                                                                      404, variables.order_not_found]])
    def test_take_order_invalid_order_id_error_invalid_data(self, order_id, error_code, error_message,
                                                            sign_up_new_courier, log_in_courier, delete_courier):
        courier_id = log_in_courier.json()['id']
        with allure.step(f'Отправка запроса PUT: Принятие заказа с id "{order_id}", id курьера "{courier_id}", '
                         f'ожидается сообщение: "{error_message}" с кодом "{error_code}"'):
            response_take_order = requests.put(f'{variables.TAKE_ORDER}/{order_id}?courierId={courier_id}')
            get_error_message = response_take_order.json()['message']
        assert response_take_order.status_code == error_code and get_error_message == error_message
