import allure
import pytest

from components.bottom_nav_bar import BottomNavBar
from pages.bg_color import BgColorPage


@allure.feature("Экран Background")
@allure.story("Проверка цветов баннеров")
@pytest.mark.bg_color_page
class TestBackgroundColors:
    @allure.title("Красный баннер имеет красный цвет")
    def test_red_half_banner_color(self, driver, tmp_path):
        page = BgColorPage(driver)
        nav_bar = BottomNavBar(driver)

        expected_color = (255, 0, 0)

        with allure.step("Открыть экран Background"):
            nav_bar.click_to_bg_color_button()

        with allure.step(
            f"Проверить, что цвет красного баннера равен {expected_color}"
        ):
            actual_color = page.get_red_half_banner_color(tmp_path)

            assert actual_color == expected_color

    @allure.title("Синий баннер имеет синий цвет")
    def test_blue_half_banner_color(self, driver, tmp_path):
        page = BgColorPage(driver)
        nav_bar = BottomNavBar(driver)

        expected_color = (0, 0, 255)

        with allure.step("Открыть экран Background"):
            nav_bar.click_to_bg_color_button()

        with allure.step(f"Проверить, что цвет синего баннера равен {expected_color}"):
            actual_color = page.get_blue_half_banner_color(tmp_path)

            assert actual_color == expected_color
