from datetime import datetime


class DataForTest:
    data_201 = {
        "login": f'test+{datetime.now().strftime("%m%d%Y%H%M%S")}',
        "password": "1234",
        "firstName": "saske"
    }

    data_409 = {
        "login": "ninja",
        "password": "1234",
        "firstName": "oleg"
    }

    data_400 = {
        "login": "",
        "password": "",
        "firstName": ""
    }

    data_login = {
        "login": "1ninja+21",
        "password": "1234"
    }

    data_not_login = {
        "login": "",
        "password": "1234"
    }

    data_fail_login_and_password = {
        "login": " ",
        "password": " "
    }

    data_not_correct = {
        "login": "",
        "password": ""
    }

    data_not_log = {
        "password": "1234"
    }

    data_for_order = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": [
            "BLACK"
        ]
    }

    data_add_color = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": [
            "BLACK",
            "GREY"
        ]
    }

    data_not_color = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha"
    }

    data_not_delivery = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "",
        "comment": "Saske, come back to Konoha",
        "color": [
            "BLACK"
        ]
    }
