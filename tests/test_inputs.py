import allure
import pytest

from components.bottom_nav_bar import BottomNavBar
from pages.inputs import InputsPage


@allure.feature("Экран Inputs")
@allure.story("Проверка работы полей ввода")
@pytest.mark.inputs_page
class TestInputs:
    @allure.title("Пользователь может ввести текст в обычное поле")
    def test_normal_input_text_typing(self, driver):
        page = InputsPage(driver)
        nav_bar = BottomNavBar(driver)

        with allure.step("Открыть экран Inputs"):
            nav_bar.click_to_inputs_button()

        with allure.step("Проверить ввод текста в обычное поле"):
            page.type_to_normal_input("Hello")

            assert page.get_normal_input_text() == "Hello"
            assert page.get_text_length() == "Text length: 5"

    @allure.title("Отображается сообщение об ошибке при вводе менее 5 символов")
    def test_validation_input_shows_error_for_short_text(self, driver):
        page = InputsPage(driver)
        nav_bar = BottomNavBar(driver)

        with allure.step("Открыть экран Inputs"):
            nav_bar.click_to_inputs_button()

        with allure.step("Проверить отображение ошибки валидации"):
            page.type_to_validation_input("abc")

            assert page.is_too_short_text_displayed()

    @allure.title("Поле Disabled недоступно для редактирования")
    def test_disabled_input_is_not_enabled(self, driver):
        page = InputsPage(driver)
        nav_bar = BottomNavBar(driver)

        with allure.step("Открыть экран Inputs"):
            nav_bar.click_to_inputs_button()

        with allure.step("Проверить, что поле Disabled недоступно"):
            assert page.get_disabled_input_text() == "Disabled input"
            assert page.is_disabled_input_enabled() is False

    @allure.title("После отключения переключателя поля становятся недоступными")
    def test_normal_and_validation_inputs_become_disabled_after_switch_off(
        self,
        driver,
    ):
        page = InputsPage(driver)
        nav_bar = BottomNavBar(driver)

        with allure.step("Открыть экран Inputs"):
            nav_bar.click_to_inputs_button()

        with allure.step("Отключить переключатель Enabled"):
            page.click_enabled_switch()

        with allure.step("Проверить, что обычное поле и поле валидации недоступны"):
            assert page.is_normal_input_enabled() is False
            assert page.is_validation_input_enabled() is False

    @allure.title("Пример падения теста со снятием скриншота")
    @pytest.mark.skip(reason="Используется для проверки скриншота при падении")
    def test_normal_input_text_typing_failed_screenshot_example(
        self,
        driver,
    ):
        page = InputsPage(driver)
        nav_bar = BottomNavBar(driver)

        with allure.step("Открыть экран Inputs"):
            nav_bar.click_to_inputs_button()

        with allure.step("Проверить, что при падении теста будет сделан скриншот"):
            page.type_to_normal_input("Hello")

            assert page.get_normal_input_text() == "Wrong text"
