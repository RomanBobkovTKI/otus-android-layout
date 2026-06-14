import pytest

from components.bottom_nav_bar import BottomNavBar
from pages.inputs import InputsPage


@pytest.mark.inputs_page
def test_normal_input_text_typing(driver):
    page = InputsPage(driver)
    nav_bar = BottomNavBar(driver)

    nav_bar.click_to_inputs_button()

    page.type_to_normal_input("Hello")

    assert page.get_normal_input_text() == "Hello"
    assert page.get_text_length() == "Text length: 5"


@pytest.mark.inputs_page
def test_validation_input_shows_error_for_short_text(driver):
    page = InputsPage(driver)
    nav_bar = BottomNavBar(driver)

    nav_bar.click_to_inputs_button()

    page.type_to_validation_input("abc")

    assert page.is_too_short_text_displayed()


@pytest.mark.inputs_page
def test_disabled_input_is_not_enabled(driver):
    page = InputsPage(driver)
    nav_bar = BottomNavBar(driver)

    nav_bar.click_to_inputs_button()

    assert page.get_disabled_input_text() == "Disabled input"
    assert page.is_disabled_input_enabled() is False


@pytest.mark.inputs_page
def test_normal_and_validation_inputs_become_disabled_after_switch_off(driver):
    page = InputsPage(driver)
    nav_bar = BottomNavBar(driver)

    nav_bar.click_to_inputs_button()

    page.click_enabled_switch()

    assert page.is_normal_input_enabled() is False
    assert page.is_validation_input_enabled() is False


@pytest.mark.inputs_page
@pytest.mark.skip(reason="for failed and take screenshot")
def test_normal_input_text_typing_failed_screenshot_example(driver):
    page = InputsPage(driver)
    nav_bar = BottomNavBar(driver)

    nav_bar.click_to_inputs_button()

    page.type_to_normal_input("Hello")

    assert page.get_normal_input_text() == "Wrong text"
