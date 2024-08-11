import requests
import random
import string
import pytest
import variables
import allure


@pytest.fixture(scope='function')
def payload_new_courier():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    # генерируем логин, пароль и имя курьера
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    # собираем тело запроса
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    return payload


@allure.step('Отправка запроса POST: Регистрация нового курьера с корректными данными')
@pytest.fixture(scope='function')
def sign_up_new_courier(payload_new_courier):
    payload = payload_new_courier
    with allure.step(f'Отправка запроса POST: Регистрация нового курьера с данными "{payload}"'):
        response_sign_up = requests.post(variables.SIGN_UP_COURIER, data=payload)
    return response_sign_up


@pytest.fixture(scope='function')
def log_in_courier(payload_new_courier):
    payload = payload_new_courier
    with allure.step(f'Отправка запроса POST: Вход курьера по '
                     f'логину "{payload['login']}" и паролю "{payload['password']}"'):
        response_login = requests.post(variables.LOGIN_COURIER, data={'login': payload['login'],
                                                                      'password': payload['password']})
    return response_login


@pytest.fixture(scope='function')
def delete_courier(log_in_courier):
    pass
    yield
    with allure.step(f'Отправка запроса DELETE: Удаление курьера по id "{log_in_courier.json()['id']}"'):
        courier_id = log_in_courier.json()['id']
        requests.delete(f'{variables.SIGN_UP_COURIER}/{courier_id}', params={'id': courier_id})


@pytest.fixture(scope='function')
def get_order():
    with allure.step(f'Отправка запроса POST: Создание заказа с данными "{variables.order_color_grey}"'):
        response_order = requests.post(variables.CREATE_ORDER, params=variables.order_color_grey)
        order_track = response_order.json()['track']
    with allure.step(f'Отправка запроса GET: Получаение заказа по его трек номеру "{order_track}"'):
        response_order = requests.get(f'{variables.GET_ORDER_VIA_TRACK_NUM}?t={order_track}')
    return response_order
