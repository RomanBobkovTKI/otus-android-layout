import logging
import os
from pathlib import Path

from appium import webdriver
from appium.options.android import UiAutomator2Options


logger = logging.getLogger(__name__)


ROOT_DIR = Path(__file__).resolve().parent.parent
DEFAULT_APK_PATH = ROOT_DIR / "app" / "app-debug.apk"


def create_driver():
    appium_server_url = os.getenv(
        "APPIUM_SERVER_URL",
        "http://127.0.0.1:4723",
    )

    apk_path = Path(
        os.getenv("APK_PATH", str(DEFAULT_APK_PATH))
    ).resolve()

    if not apk_path.exists():
        raise FileNotFoundError(f"APK file not found: {apk_path}")

    logger.debug("Creating Appium driver")
    logger.debug("Appium server URL: %s", appium_server_url)
    logger.debug("APK path: %s", apk_path)

    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.device_name = os.getenv("DEVICE_NAME", "Android Emulator")

    options.app = str(apk_path)

    options.auto_grant_permissions = True
    options.no_reset = False
    options.full_reset = False

    driver = webdriver.Remote(
        command_executor=appium_server_url,
        options=options,
    )

    logger.debug("Appium driver created. Session id: %s", driver.session_id)

    return driver