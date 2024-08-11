import allure
import pytest
import requests
import variables


class TestCreateOrder:

    @allure.title('Запрос POST "Создание заказа"')
    @pytest.mark.parametrize('payload', [variables.order_color_grey,
                                         variables.order_color_black,
                                         variables.order_multiple_colors,
                                         variables.order_no_colors])
    def test_post_new_order_receive_order_track(self, payload):
        with allure.step(f'Отправка запроса POST: Создание заказа с данными "{payload}, '
                         f'ожидается вывод сообщения с треком заказа и с кодом "201"'):
            response_order = requests.post(variables.CREATE_ORDER, params=payload)
        assert response_order.status_code == 201 and response_order.json()['track']
