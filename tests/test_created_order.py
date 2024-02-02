import allure
import pytest
import requests

from data_test.constants import Constants
from data_test.user_data import DataForTest

base_url = f'{Constants.URL}'
end_point = f'{Constants.END_POINT_ORDERS}'
headers = {"Content-Type": "application/json"}


@allure.epic("Тестирование АПИ")
@allure.feature("Создание заказа")
class TestCreateOrder:

    @allure.story("Тестирование создания заказа")
    @allure.title('Корректный ответ системы на валидные и не валидные данные')
    @allure.description(
        "В этом тесте проверяются ответы системы на валидные данные, "
        "наличие слова track в теле ответа")
    @allure.tag("NewAPI", "Essentials", "CreatOrder")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label("owner", "Kozlov Oleg")
    @allure.link("https://qa-scooter.praktikum-services.ru", name="Website")
    @allure.issue("CreatOrder-03")
    @allure.testcase("TMS-03")
    @allure.step("Отправка валыдного POST запроса с набором тестовых данных для создания заказа")
    @pytest.mark.parametrize(("data", "status_code"), [
        (
                pytest.param(DataForTest.data_for_order, 201)
        ),
        (
                pytest.param(DataForTest.data_add_color, 201)
        ),
        (
                pytest.param(DataForTest.data_not_color, 201)
        )
    ])
    def test_create_courier(self, data, status_code):
        response = requests.post(base_url + end_point, headers=headers, json=data)
        assert response.status_code == status_code
        assert 'track' in response.json()

    @allure.story("Тестирование создания заказа")
    @allure.title('Корректный ответ системы на не валидные данные')
    @allure.description(
        "В этом тесте проверяются ответы системы на не валидные данные, статус код и текст ошибки")
    @allure.tag("NewAPI", "Essentials", "CreatOrder")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label("owner", "Kozlov Oleg")
    @allure.link("https://qa-scooter.praktikum-services.ru", name="Website")
    @allure.issue("CreatOrder-03")
    @allure.testcase("TMS-03")
    @allure.step("Отправка невалидного POST запроса с набором тестовых данных для создания заказа")
    @pytest.mark.parametrize(("data", "status_code"), [
        (
                pytest.param(DataForTest.data_not_delivery, 500)
        )
    ])
    def test_create_courier_fail(self, data, status_code):
        response = requests.post(base_url + end_point, headers=headers, json=data)
        assert response.json() == {"code": 500, "message": "invalid input syntax for type timestamp with "
                                                           "time zone: \"Invalid date\""}
