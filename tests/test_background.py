import pytest

from components.bottom_nav_bar import BottomNavBar
from pages.bg_color import BgColorPage


@pytest.mark.bg_color_page
def test_red_half_banner_color(driver, tmp_path):
    page = BgColorPage(driver)
    nav_bar = BottomNavBar(driver)

    expected_color = (255, 0, 0)

    nav_bar.click_to_bg_color_button()

    actual_color = page.get_red_half_banner_color(tmp_path)

    assert expected_color == actual_color


@pytest.mark.bg_color_page
def test_blue_half_banner_color(driver, tmp_path):
    page = BgColorPage(driver)
    nav_bar = BottomNavBar(driver)

    expected_color = (0, 0, 255)

    nav_bar.click_to_bg_color_button()

    actual_color = page.get_blue_half_banner_color(tmp_path)

    assert expected_color == actual_color
