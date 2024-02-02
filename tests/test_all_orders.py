import allure
import requests

from data_test.constants import Constants

base_url = f'{Constants.URL}'
end_point = f'{Constants.END_POINT_ORDERS}'
headers = {"Content-Type": "application/json"}

@allure.epic("Тестирование АПИ")
@allure.feature("Выгрузка всех заказов")
class TestGetAllOrder:
    @allure.story("GET запрос на выгрузку всех заказов в системе")
    @allure.title('Успешная выгрузка всех заказов')
    @allure.description("Этот тест проверяет успешную выгрузку всех заказов в системе")
    @allure.tag("NewAPI", "Essentials", "GetAllOrders")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label("owner", "Kozlov Oleg")
    @allure.link("https://qa-scooter.praktikum-services.ru", name="Website")
    @allure.issue("GetOrders-01")
    @allure.testcase("TMS-02")
    @allure.step("Отправка GET запроса с заголовком")
    def test_get_all_order(self):
        response = requests.get(base_url + end_point, headers=headers)
        assert response.status_code == 200
        result = response.json()
        assert type(result['orders'][0]) == dict