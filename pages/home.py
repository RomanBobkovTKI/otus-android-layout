from appium.webdriver.common.appiumby import AppiumBy

from pages.base import BasePage


class HomePage(BasePage):
    HOME_TEXT = (AppiumBy.ACCESSIBILITY_ID, "home_text")

    def is_home_screen_opened(self):
        return self.is_displayed(self.HOME_TEXT)

    def get_home_text(self):
        return self.find(self.HOME_TEXT).text.lower().strip()
