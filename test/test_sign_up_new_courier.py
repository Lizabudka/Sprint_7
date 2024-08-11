import allure
import pytest
import requests
import variables


class TestCourierSignUp:

    @allure.title('Запрос POST "Создание курьера" с корректными данными')
    def test_courier_sign_up_valid_data_signed_up(self, sign_up_new_courier, delete_courier):
        response_sign_up = sign_up_new_courier
        assert response_sign_up.status_code == 201 and response_sign_up.json()['ok'] is True

    @allure.title('Запрос POST "Создание курьера" с одинаковыми данными дважды')
    def test_courier_sign_up_valid_data_used_twice_error_login_is_occupied(self, sign_up_new_courier,
                                                                           payload_new_courier,
                                                                           delete_courier):
        response_sign_up = sign_up_new_courier
        assert response_sign_up.status_code == 201 and response_sign_up.json()['ok'] is True

        payload = payload_new_courier
        with allure.step(f'Запрос POST: Логин курьера с теми же данными повторно, '
                         f'ожидается вывод сообщения "{variables.login_is_used}" с кодом "409"'):
            response = requests.post(variables.SIGN_UP_COURIER, data=payload)
            response_message = response.json()
        assert response.status_code == 409 and response_message['message'] == variables.login_is_used

    @allure.title('Запрос POST "Создание курьера" с пустыми полями')
    @pytest.mark.parametrize('login, password', [[variables.courier_example[0], ''],
                                                 ['', variables.courier_example[1]]])
    def test_courier_sign_up_required_field_is_empty_error_not_enough_data(self, login, password):
        with allure.step(f'Запрос POST: Логин курьера с логином "{login}", паролем "{password}", '
                         f'ожидается вывод сообщения "{variables.sign_up_field_is_empty}" с кодом "400"'):
            response_sigh_up = requests.post(variables.SIGN_UP_COURIER, data={'login': login,
                                                                              'password': password})
            error_message = response_sigh_up.json()['message']
        assert response_sigh_up.status_code == 400 and error_message == variables.sign_up_field_is_empty
