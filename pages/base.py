import logging

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


logger = logging.getLogger(__name__)


class BasePage:
    DEFAULT_TIMEOUT = 10

    def __init__(self, driver, timeout=DEFAULT_TIMEOUT):
        self.driver = driver
        self.timeout = timeout

    def get_element(self, locator, timeout=None):
        wait_timeout = timeout or self.timeout

        logger.debug("Searching element: %s, timeout=%s", locator, wait_timeout)

        return WebDriverWait(self.driver, wait_timeout).until(
            EC.presence_of_element_located(locator)
        )

    def get_visible_element(self, locator, timeout=None):
        wait_timeout = timeout or self.timeout

        logger.debug("Searching visible element: %s, timeout=%s", locator, wait_timeout)

        return WebDriverWait(self.driver, wait_timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def get_clickable_element(self, locator, timeout=None):
        wait_timeout = timeout or self.timeout

        logger.debug(
            "Searching clickable element: %s, timeout=%s", locator, wait_timeout
        )

        return WebDriverWait(self.driver, wait_timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def click(self, locator, timeout=None):
        logger.debug("Click element: %s", locator)
        self.get_clickable_element(locator, timeout).click()

    def type_text(self, locator, text, timeout=None):
        logger.debug("Type text into element: %s, text=%s", locator, text)

        element = self.get_visible_element(locator, timeout)
        element.clear()
        element.send_keys(text)

    def is_displayed(self, locator, timeout=None):
        logger.debug("Check element is displayed: %s", locator)

        try:
            return self.get_visible_element(locator, timeout).is_displayed()
        except TimeoutException:
            logger.debug("Element is not displayed: %s", locator)
            return False
