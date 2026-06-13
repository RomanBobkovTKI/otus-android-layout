from appium.webdriver.common.appiumby import AppiumBy


from pages.base import BasePage


class DpPage(BasePage):
    HEADER_TEXT = (AppiumBy.XPATH, '//android.widget.TextView[@text="DP vs PX Demo"]')

    def get_header_text(self):
        return self.get_visible_element(self.HEADER_TEXT).text.lower().strip()
