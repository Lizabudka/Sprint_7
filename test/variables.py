
SIGN_UP_COURIER = 'https://qa-scooter.praktikum-services.ru/api/v1/courier'
LOGIN_COURIER = 'https://qa-scooter.praktikum-services.ru/api/v1/courier/login'
CREATE_ORDER = 'https://qa-scooter.praktikum-services.ru/api/v1/orders'
GET_LIST_OF_ORDERS = 'https://qa-scooter.praktikum-services.ru/api/v1/orders'
TAKE_ORDER = 'https://qa-scooter.praktikum-services.ru/api/v1/orders/accept'
GET_ORDER_VIA_TRACK_NUM = 'https://qa-scooter.praktikum-services.ru/api/v1/orders/track'

login_is_used = 'Этот логин уже используется. Попробуйте другой.'
sign_up_field_is_empty = 'Недостаточно данных для создания учетной записи'
log_in_field_is_empty = 'Недостаточно данных для входа'
login_not_found = 'Учетная запись не найдена'
no_such_courier = 'Курьера с таким id нет.'
del_no_id_field = 'Недостаточно данных для удаления курьера'
order_empty_data = 'Недостаточно данных для поиска'
order_not_found = 'Заказа с таким id не существует'
order_no_such_courier = 'Курьера с таким id не существует'
oreder_not_found_via_track = 'Заказ не найден'

courier_example = [{"login": "bulochka"}, {"password": "skoritsey"}]

order_color_grey = {"firstName": "Naruto",
                    "lastName": "Uchiha",
                    "address": "Konoha, 142 apt.",
                    "metroStation": 4,
                    "phone": "+7 800 355 35 35",
                    "rentTime": 5,
                    "deliveryDate": "2024-06-06",
                    "comment": "Saske, come back to Konoha",
                    "color": ["GREY"]}

order_color_black = {"firstName": "Naruto",
                     "lastName": "Uchiha",
                     "address": "Konoha, 142 apt.",
                     "metroStation": 4,
                     "phone": "+7 800 355 35 35",
                     "rentTime": 5,
                     "deliveryDate": "2024-06-06",
                     "comment": "Saske, come back to Konoha",
                     "color": ["BLACK"]}

order_multiple_colors = {"firstName": "Naruto",
                         "lastName": "Uchiha",
                         "address": "Konoha, 142 apt.",
                         "metroStation": 4,
                         "phone": "+7 800 355 35 35",
                         "rentTime": 5,
                         "deliveryDate": "2024-06-06",
                         "comment": "Saske, come back to Konoha",
                         "color": ["BLACK", "GREY"]}
order_no_colors = {"firstName": "Naruto",
                   "lastName": "Uchiha",
                   "address": "Konoha, 142 apt.",
                   "metroStation": 4,
                   "phone": "+7 800 355 35 35",
                   "rentTime": 5,
                   "deliveryDate": "2024-06-06",
                   "comment": "Saske, come back to Konoha",
                   "color": []}

orders_payload = {'limit': 4, 'page': 0}
