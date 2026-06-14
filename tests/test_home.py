import allure
import pytest

from pages.home import HomePage


@allure.feature("Главный экран")
@allure.story("Проверка главного экрана")
@pytest.mark.home_screen
class TestHomeScreen:
    @allure.title("Главный экран отображается")
    def test_home_screen_is_displayed(self, driver):
        with allure.step("Открыть главную страницу"):
            home_page = HomePage(driver)

        with allure.step("Проверить, что главный экран открыт"):
            assert home_page.is_home_screen_opened()

    @allure.title("Текст на главном экране соответствует ожидаемому")
    def test_home_screen_text(self, driver):
        with allure.step("Открыть главную страницу"):
            home_page = HomePage(driver)

        expected_text = "home screen"

        with allure.step("Проверить текст на главном экране = home screen"):
            actual_text = home_page.get_home_text()

            assert actual_text == expected_text
