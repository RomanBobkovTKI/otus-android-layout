from appium import webdriver
from appium.options.android import UiAutomator2Options


def create_driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.device_name = "Android Emulator"

    options.app_package = "com.example.layout_android"
    options.app_activity = ".MainActivity"

    options.auto_grant_permissions = True
    options.no_reset = False
    options.full_reset = False

    return webdriver.Remote(command_executor="http://127.0.0.1:4723", options=options)
