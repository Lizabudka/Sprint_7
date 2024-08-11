import allure
import requests
import variables


class TestDeleteCourier:

    @allure.title('Запрос DELETE "Удаление курьера" для зарегистрированного курьера с корректным id')
    def test_delete_courier_valid_data_courier_is_deleted(self, sign_up_new_courier, log_in_courier):
        courier_id = log_in_courier.json()['id']
        with allure.step(f'Отправка запроса DELETE: Удаление курьера с id "{courier_id}", '
                         f'ожидается сообщение "ok: true" с кодом "200"'):
            response_del = requests.delete(f'{variables.SIGN_UP_COURIER}/{courier_id}', params={'id': courier_id})
        assert response_del.status_code == 200 and response_del.json()['ok'] is True

    @allure.title('Запрос DELETE "Удаление курьера" для незарегистрированного курьера')
    def test_delete_courier_wrong_id_error_nonexistent_courier(self, sign_up_new_courier, log_in_courier,
                                                               delete_courier):
        courier_id = log_in_courier.json()['id']
        with allure.step(f'Отправка запроса DELETE: Удаление курьера с id "{courier_id}007", '
                         f'ожидается сообщение "{variables.no_such_courier}" с кодом "404"'):
            response_del = requests.delete(f'{variables.SIGN_UP_COURIER}/{courier_id}007',
                                           params={'id': f'{courier_id}007'})
        assert response_del.status_code == 404 and response_del.json()['message'] == variables.no_such_courier

    @allure.title('Запрос DELETE "Удаление курьера" с незаполненным параметром id')
    def test_delete_courier_no_id_request_error_no_required_field(self):
        with allure.step(f'Отправка запроса DELETE: Удаление курьера с пустым  id, '
                         f'ожидается сообщение "{variables.del_no_id_field}" с кодом "400"'):
            response_del = requests.delete(f'{variables.SIGN_UP_COURIER}/')
        assert response_del.status_code == 400 and response_del.json()['message'] == variables.del_no_id_field
