import logging

from appium import webdriver
from appium.options.android import UiAutomator2Options


logger = logging.getLogger(__name__)


def create_driver():
    logger.debug("Creating Appium driver")

    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.device_name = "Android Emulator"

    options.app_package = "com.example.layout_android"
    options.app_activity = ".MainActivity"

    options.auto_grant_permissions = True
    options.no_reset = False
    options.full_reset = False

    driver = webdriver.Remote(
        command_executor="http://127.0.0.1:4723",
        options=options,
    )

    logger.debug("Appium driver created. Session id: %s", driver.session_id)

    return driver
