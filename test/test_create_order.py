import allure
import pytest
import requests
import variables
import random


class TestGetOrder:

    @allure.title('Запрос GET "Получить заказ по его номеру" для заказа с корректным трек-номером')
    def test_get_order_via_track_num_valid_data_status_ok(self, get_order):
        assert get_order.status_code == 200 and get_order.json()['order']

    @allure.title('Запрос GET "Получить заказ по его номеру" для заказа с некорректным трек-номером')
    @pytest.mark.parametrize('order_num, error_code, error_message', [['', 400, variables.order_empty_data],
                                                                      [random.randrange(1111111, 9999999),
                                                                       404, variables.oreder_not_found_via_track]])
    def test_get_order_via_track_num_invalid_data_error_invalid_data(self, order_num,
                                                                     error_code, error_message):
        with allure.step(f'Отправка запроса GET: Получение заказа по номеру "{order_num}", '
                         f'ожидается ошибка "{error_message}" с кодом "{error_code}"'):
            response_order = requests.get(f'{variables.GET_ORDER_VIA_TRACK_NUM}?t={order_num}')
            get_error_message = response_order.json()['message']
        assert response_order.status_code == error_code and get_error_message == error_message
