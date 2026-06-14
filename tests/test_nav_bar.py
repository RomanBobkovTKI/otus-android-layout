import allure
import pytest

from components.bottom_nav_bar import BottomNavBar
from pages.bg_color import BgColorPage
from pages.dp import DpPage
from pages.inputs import InputsPage
from pages.text import TextPage


@allure.feature("Нижняя навигационная панель")
@allure.story("Проверка отображения и текста кнопок")
@pytest.mark.nav_bar
class TestBottomNavBar:
    @allure.title("Все кнопки нижней панели отображаются")
    def test_nav_bar_buttons_is_displayed(self, driver):
        nav_bar = BottomNavBar(driver)

        with allure.step("Проверить отображение всех кнопок нижней панели"):
            assert nav_bar.dp_button_is_displayed()
            assert nav_bar.text_button_is_displayed()
            assert nav_bar.bg_color_button_is_displayed()
            assert nav_bar.inputs_button_is_displayed()

    @allure.title("Текст кнопки DP соответствует ожидаемому")
    def test_dp_button_text(self, driver):
        nav_bar = BottomNavBar(driver)

        expected_text = "dp"

        with allure.step(f"Проверить, что текст кнопки DP равен '{expected_text}'"):
            actual_text = nav_bar.get_dp_button_text()

            assert actual_text == expected_text

    @allure.title("Текст кнопки Text соответствует ожидаемому")
    def test_text_button_text(self, driver):
        nav_bar = BottomNavBar(driver)

        expected_text = "text"

        with allure.step(f"Проверить, что текст кнопки Text равен '{expected_text}'"):
            actual_text = nav_bar.get_text_button_text()

            assert actual_text == expected_text

    @allure.title("Текст кнопки BG Color соответствует ожидаемому")
    def test_bg_color_button_text(self, driver):
        nav_bar = BottomNavBar(driver)

        expected_text = "bg_color"

        with allure.step(
            f"Проверить, что текст кнопки BG Color равен '{expected_text}'"
        ):
            actual_text = nav_bar.bg_color_button_text()

            assert actual_text == expected_text

    @allure.title("Текст кнопки Inputs соответствует ожидаемому")
    def test_input_button_text(self, driver):
        nav_bar = BottomNavBar(driver)

        expected_text = "inputs"

        with allure.step(f"Проверить, что текст кнопки Inputs равен '{expected_text}'"):
            actual_text = nav_bar.get_inputs_button_text()

            assert actual_text == expected_text


@allure.feature("Нижняя навигационная панель")
@allure.story("Переходы между экранами")
@pytest.mark.nav_bar
class TestBottomNavBarNavigation:
    @allure.title("Открывается экран DP")
    @pytest.mark.dp_page
    def test_open_dp_page(self, driver):
        nav_bar = BottomNavBar(driver)
        dp_page = DpPage(driver)

        expected_text = "dp vs px demo"

        with allure.step("Нажать на кнопку DP"):
            nav_bar.click_to_dp_button()

        with allure.step(f"Проверить, что открыт экран с заголовком '{expected_text}'"):
            actual_text = dp_page.get_header_text()

            assert actual_text == expected_text

    @allure.title("Открывается экран Text")
    @pytest.mark.text_page
    def test_open_text_page(self, driver):
        nav_bar = BottomNavBar(driver)
        text_page = TextPage(driver)

        expected_text = "demo text"

        with allure.step("Нажать на кнопку Text"):
            nav_bar.click_to_text_button()

        with allure.step(f"Проверить, что открыт экран с заголовком '{expected_text}'"):
            actual_text = text_page.get_header_text()

            assert actual_text == expected_text

    @allure.title("Открывается экран Background")
    @pytest.mark.bg_color_page
    def test_open_bg_color_page(self, driver):
        nav_bar = BottomNavBar(driver)
        bg_color_page = BgColorPage(driver)

        expected_text = "background demo"

        with allure.step("Нажать на кнопку BG Color"):
            nav_bar.click_to_bg_color_button()

        with allure.step(f"Проверить, что открыт экран с заголовком '{expected_text}'"):
            actual_text = bg_color_page.get_header_text()

            assert actual_text == expected_text

    @allure.title("Открывается экран Inputs")
    @pytest.mark.inputs_page
    def test_open_inputs_page(self, driver):
        nav_bar = BottomNavBar(driver)
        inputs_page = InputsPage(driver)

        expected_text = "input playground"

        with allure.step("Нажать на кнопку Inputs"):
            nav_bar.click_to_inputs_button()

        with allure.step(f"Проверить, что открыт экран с заголовком '{expected_text}'"):
            actual_text = inputs_page.get_header_text()

            assert actual_text == expected_text
