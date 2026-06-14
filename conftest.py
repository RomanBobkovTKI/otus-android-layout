from datetime import datetime

import pytest
from utils.driver_factory import create_driver
from pathlib import Path


SCREENSHOTS_DIR = Path("screenshots")


@pytest.fixture
def driver():
    driver = create_driver()
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")

        if driver is None:
            return

        SCREENSHOTS_DIR.mkdir(exist_ok=True)

        test_name = item.name
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        screenshot_path = SCREENSHOTS_DIR / f"{test_name}_{timestamp}.png"

        driver.save_screenshot(str(screenshot_path))

        print(f"\nScreenshot saved: {screenshot_path}")
