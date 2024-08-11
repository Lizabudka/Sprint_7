import allure
import requests
import variables


class TestGetOrdersList:

    @allure.title('Запрос GET "Получение списка заказов"')
    def test_get_list_of_orders_receive_list_of_orders(self):
        payload = [variables.order_color_grey,
                   variables.order_color_black,
                   variables.order_multiple_colors,
                   variables.order_no_colors]
        with allure.step(f'Отправка запроса POST: Создание 4-х заказов"'):
            for i in range(4):
                requests.post(variables.CREATE_ORDER, params=payload[i])
        with allure.step(f'Отправка запроса GET: Получение списка заказов, '
                         f'ожидается вывод сообщения с кол-вом заказов "4" и с кодом "200"'):
            response_orders_list = requests.get(variables.GET_LIST_OF_ORDERS, params=variables.orders_payload)
            orders = response_orders_list.json()['orders']
        assert response_orders_list.status_code == 200 and len(orders) == 4
