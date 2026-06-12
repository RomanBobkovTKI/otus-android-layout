import pytest

from components.bottom_nav_bar import BottomNavBar


@pytest.mark.nav_bar
def test_nav_bar_button_is_displayed(driver):
    nav_bar = BottomNavBar(driver)

    assert nav_bar.dp_button_is_displayed()
    assert nav_bar.text_button_is_displayed()


@pytest.mark.nav_bar
def test_dp_button_text(driver):
    nav_bar = BottomNavBar(driver)

    expected_test = "dp"

    actual_text = nav_bar.get_dp_button_text()

    assert expected_test == actual_text


@pytest.mark.nav_bar
def test_text_button_text(driver):
    nav_bar = BottomNavBar(driver)

    expected_test = "text"

    actual_text = nav_bar.get_text_button_text()

    assert expected_test == actual_text
