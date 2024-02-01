import allure
import pytest
import requests

from data_test.constants import Constants
from data_test.user_data import DataForTest


base_url = f'{Constants.URL}'
headers = {"Content-Type": "application/json"}


@allure.epic("Тестирование АПИ")
@allure.feature("Авторизация курьера")
class TestLoginCourier:

    @allure.story("POST запрос - Авторизация курьера в системе")
    @allure.title('Проверка авторизации в системе с валидными и невалидными данными')
    @allure.description("В этом тесте проверяются валидные и не валидные данные для авторизации. Авторизация возможна"
                        "с корректными данными. Система возвращает корректные стаус коды и тексты ошибок на "
                        "НЕвалидные данные")
    @allure.tag("NewAPI", "Essentials", "LoginCourier")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label("owner", "Kozlov Oleg")
    @allure.link("https://qa-scooter.praktikum-services.ru", name="Website")
    @allure.issue("LoginCourier-01")
    @allure.testcase("TMS-03")
    @allure.step("Отправка POST запроса - с валидными и невалидными данными")
    @pytest.mark.parametrize(("data", "status_code", "json"), [
        (
                pytest.param(DataForTest.data_login, 200, {'id': 253230})
        ),
        (
                pytest.param(DataForTest.data_not_login, 400,
                             {'code': 400, 'message': 'Недостаточно данных для входа'})
        ),
        (
                pytest.param(DataForTest.data_fail_login_and_password, 404,
                             {"code": 404, "message": "Учетная запись не найдена"})
        ),
        (
                pytest.param(DataForTest.data_not_correct, 400,
                             {"code": 400, "message": "Недостаточно данных для входа"})
        ),
        (
                pytest.param(DataForTest.data_not_log, 400,
                             {"code": 400, "message": "Недостаточно данных для входа"})
        ),
    ])
    def test_login_courier_correct(self, data, status_code, json):
        response = requests.post(base_url + "/api/v1/courier/login", headers=headers, json=data)
        assert response.status_code == status_code
        assert response.json() == json