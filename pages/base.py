from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    DEFAULT_TIMEOUT = 10

    def __init__(self, driver, timeout=DEFAULT_TIMEOUT):
        self.driver = driver
        self.timeout = timeout

    def get_element(self, locator, timeout=None):
        return WebDriverWait(
            self.driver,
            timeout or self.timeout
        ).until(
            EC.presence_of_element_located(locator)
        )

    def get_visible_element(self, locator, timeout=None):
        return WebDriverWait(
            self.driver,
            timeout or self.timeout
        ).until(
            EC.visibility_of_element_located(locator)
        )

    def get_clickable_element(self, locator, timeout=None):
        return WebDriverWait(
            self.driver,
            timeout or self.timeout
        ).until(
            EC.element_to_be_clickable(locator)
        )

    def click(self, locator, timeout=None):
        self.get_clickable_element(locator, timeout).click()

    def type_text(self, locator, text, timeout=None):
        element = self.get_visible_element(locator, timeout)
        element.clear()
        element.send_keys(text)

    def is_displayed(self, locator, timeout=None):
        try:
            return self.get_visible_element(locator, timeout).is_displayed()
        except TimeoutException:
            return False