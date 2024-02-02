import allure
import pytest
import requests

from data_test.user_data import DataForTest
from data_test.constants import Constants

base_url = f'{Constants.URL}'
end_point_creat_courier = f'{Constants.END_POINT_CREAT_COURIER}'
headers = {"Content-Type": "application/json"}


@allure.epic("Тестирование АПИ")
@allure.feature("Создание курьера")
class TestCreateCourier:

    @allure.story("POST запрос на создание нового курьера в системе")
    @allure.title('Тестирование валидации при создании нового курьера в системе')
    @allure.description("В этом тесте проходит валидация статус кодов и тела ответа."
                        " Статус 201 ok: True")
    @allure.tag("NewAPI", "Essentials", "CreatCourier")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label("owner", "Kozlov Oleg")
    @allure.link("https://qa-scooter.praktikum-services.ru", name="Website")
    @allure.issue("CREAT-01")
    @allure.testcase("TMS-01")
    @allure.step("Отправка POST запроса с заголовком и данными нового курьера")
    @pytest.mark.parametrize(("data", "status_code", "json"), [
        (
                pytest.param(DataForTest.data_201, 201, {"ok": True})
        )
    ])
    def test_create_courier(self, data, status_code, json):
        response = requests.post(base_url + end_point_creat_courier, headers=headers, json=data)
        assert response.status_code == status_code
        assert response.json() == json

    @allure.story("POST запрос на создание нового курьера в системе")
    @allure.title('Тестирование валидации при создании нового курьера в системе')
    @allure.description("В этом тесте проходит валидация статус кодов и тела ответа."
                        " Статус 201 ok: True / "
                        "code: 409, message: Этот логин уже используется. Попробуйте другой. / "
                        "code: 400, message: Недостаточно данных для создания учетной записи")
    @allure.tag("NewAPI", "Essentials", "CreatCourier")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label("owner", "Kozlov Oleg")
    @allure.link("https://qa-scooter.praktikum-services.ru", name="Website")
    @allure.issue("CREAT-01")
    @allure.testcase("TMS-01")
    @allure.step("Отправка POST запроса с заголовком и данными нового курьера")
    @pytest.mark.parametrize(("data", "status_code", "json"), [
        (
                pytest.param(DataForTest.data_409, 409,
                             {"code": 409, "message": "Этот логин уже используется. Попробуйте другой."})
        ),
        (
                pytest.param(DataForTest.data_400, 400,
                             {"code": 400, "message": "Недостаточно данных для создания учетной записи"})
        )
    ])
    def test_create_courier_fail(self, data, status_code, json):
        response = requests.post(base_url + end_point_creat_courier, headers=headers, json=data)
        assert response.status_code == status_code
        assert response.json() == json
