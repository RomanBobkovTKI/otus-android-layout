import logging
from datetime import datetime
from pathlib import Path

import allure
import pytest

from utils.driver_factory import create_driver
from utils.logger import configure_logger


configure_logger()

SCREENSHOTS_DIR = Path("screenshots")

logger = logging.getLogger(__name__)


@pytest.fixture
def driver():
    logger.debug("Start driver fixture")

    driver = create_driver()

    yield driver

    logger.debug("Quit driver")
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")

        if driver is None:
            logger.debug("Driver fixture not found. Screenshot skipped.")
            return

        SCREENSHOTS_DIR.mkdir(exist_ok=True)

        test_name = item.name
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_path = SCREENSHOTS_DIR / f"{test_name}_{timestamp}.png"

        driver.save_screenshot(str(screenshot_path))

        logger.debug("Screenshot saved: %s", screenshot_path)

        allure.attach.file(
            str(screenshot_path),
            name="Failure screenshot",
            attachment_type=allure.attachment_type.PNG,
        )

        print(f"\nScreenshot saved: {screenshot_path}")
