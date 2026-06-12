import pytest

from pages.home import HomePage


@pytest.mark.home_screen
def test_home_screen_is_displayed(driver):
    home_page = HomePage(driver)

    assert home_page.is_home_screen_opened()


@pytest.mark.home_screen
def test_home_screen_text(driver):
    home_page = HomePage(driver)
    expected_text = "home screen"

    actual_text = home_page.get_home_text()

    assert expected_text == actual_text
