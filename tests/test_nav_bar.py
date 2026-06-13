import pytest

from components.bottom_nav_bar import BottomNavBar
from pages.bg_color import BgColorPage
from pages.dp import DpPage
from pages.inputs import InputsPage
from pages.text import TextPage


@pytest.mark.nav_bar
def test_nav_bar_buttons_is_displayed(driver):
    nav_bar = BottomNavBar(driver)

    assert nav_bar.dp_button_is_displayed()
    assert nav_bar.text_button_is_displayed()
    assert nav_bar.bg_color_button_is_displayed()
    assert nav_bar.inputs_button_is_displayed()


@pytest.mark.nav_bar
def test_dp_button_text(driver):
    nav_bar = BottomNavBar(driver)

    expected_text = "dp"

    actual_text = nav_bar.get_dp_button_text()

    assert expected_text == actual_text


@pytest.mark.nav_bar
def test_text_button_text(driver):
    nav_bar = BottomNavBar(driver)

    expected_text = "text"

    actual_text = nav_bar.get_text_button_text()

    assert expected_text == actual_text


@pytest.mark.nav_bar
def test_bg_color_button_text(driver):
    nav_bar = BottomNavBar(driver)

    expected_text = "bg_color"

    actual_text = nav_bar.bg_color_button_text()

    assert expected_text == actual_text


@pytest.mark.nav_bar
def test_input_button_text(driver):
    nav_bar = BottomNavBar(driver)

    expected_text = "inputs"

    actual_text = nav_bar.get_inputs_button_text()

    assert expected_text == actual_text


@pytest.mark.nav_bar
@pytest.mark.dp_page
def test_open_dp_page(driver):
    nav_bar = BottomNavBar(driver)
    dp_page = DpPage(driver)

    expected_text = "dp vs px demo"

    nav_bar.click_to_dp_button()

    actual_text = dp_page.get_header_text()

    assert expected_text == actual_text


@pytest.mark.nav_bar
@pytest.mark.text_page
def test_open_text_page(driver):
    nav_bar = BottomNavBar(driver)
    text_page = TextPage(driver)

    expected_text = "demo text"

    nav_bar.click_to_text_button()

    actual_text = text_page.get_header_text()

    assert expected_text == actual_text


@pytest.mark.nav_bar
@pytest.mark.bg_color_page
def test_open_bg_color_page(driver):
    nav_bar = BottomNavBar(driver)
    bg_color_page = BgColorPage(driver)

    expected_text = "background demo"

    nav_bar.click_to_bg_color_button()

    actual_text = bg_color_page.get_header_text()

    assert expected_text == actual_text


@pytest.mark.nav_bar
@pytest.mark.inputs_page
def test_open_inputs_page(driver):
    nav_bar = BottomNavBar(driver)
    inputs_page = InputsPage(driver)

    expected_text = "input playground"

    nav_bar.click_to_inputs_button()

    actual_text = inputs_page.get_header_text()

    assert expected_text == actual_text
