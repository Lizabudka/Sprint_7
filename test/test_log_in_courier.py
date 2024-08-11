import allure
import pytest
import variables
import requests


class TestLogInCourier:

    @allure.title('Запрос POST "Логин курьера в системе" с корректными данными')
    def test_log_in_courier_valid_data_logged_in(self, sign_up_new_courier, log_in_courier, delete_courier):
        response_log_in = log_in_courier
        assert response_log_in.status_code == 200 and response_log_in.json()['id']

    @allure.title('Запрос POST "Логин курьера в системе" с пустыми полями')
    @pytest.mark.parametrize('login, password', [[variables.courier_example[0], ''],
                                                 ['', variables.courier_example[1]]])
    def test_log_in_courier_required_field_is_empty_error_not_enough_data(self, login, password):
        with allure.step(f'Отправка запроса POST: логин курьера с логином "{login}" и паролем "{password}", '
                         f'ожидается вывод сообщения "{variables.log_in_field_is_empty}" и с кодом "400"'):
            response_empty_login = requests.post(variables.LOGIN_COURIER, data={"login": login,
                                                                                "password": password})
            error_message = response_empty_login.json()['message']
        assert response_empty_login.status_code == 400 and error_message == variables.log_in_field_is_empty

    @allure.title('Запрос POST "Логин курьера в системе" с незарегистрированным курьером')
    def test_log_in_nonexistent_courier_no_such_login(self, log_in_courier):
        with allure.step(f'Отправка запроса POST: вход незарегистрированного курьера, '
                         f'ожидается вывод сообщения "{variables.login_not_found}" с кодом "404"'):
            response_log_in = log_in_courier
            error_message = response_log_in.json()['message']
        assert response_log_in.status_code == 404 and error_message == variables.login_not_found

    @allure.title('Запрос POST "Логин курьера в системе" с неверным логином/паролем')
    @pytest.mark.parametrize('login_add, password_add', [['', 'add'], ['add', '']])
    def test_log_in_invalid_data_error_no_such_login(self, login_add, password_add, payload_new_courier,
                                                     sign_up_new_courier, delete_courier):

        login = payload_new_courier['login'] + login_add
        password = payload_new_courier['password'] + password_add
        with allure.step(f'Запрос POST: Логин курьера с некорректными данными -  '
                         f'логин "{login}{login_add}", пароль "{password}{password_add}", '
                         f'ожидается вывод сообщения "{variables.login_not_found}" с кодом "404"'):
            response_log_in = requests.post(variables.LOGIN_COURIER, data={'login': login,
                                                                           'password': password})
            error_message = response_log_in.json()['message']
        assert response_log_in.status_code == 404 and error_message == variables.login_not_found
