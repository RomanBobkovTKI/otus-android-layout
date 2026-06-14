from appium.webdriver.common.appiumby import AppiumBy

from pages.base import BasePage


class InputsPage(BasePage):
    HEADER_TEXT = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@text="Input Playground"]',
    )

    ENABLED_SWITCH = (
        AppiumBy.XPATH,
        "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[1]/android.view.View[1]",
    )

    NORMAL_INPUT = (
        AppiumBy.XPATH,
        "(//android.widget.EditText)[1]",
    )

    VALIDATION_INPUT = (
        AppiumBy.XPATH,
        "(//android.widget.EditText)[2]",
    )

    DISABLED_INPUT = (
        AppiumBy.XPATH,
        "(//android.widget.EditText)[3]",
    )

    TOO_SHORT_TEXT = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@text="Too short"]',
    )

    TEXT_LENGTH = (
        AppiumBy.XPATH,
        '//android.widget.TextView[contains(@text, "Text length:")]',
    )

    def get_header_text(self):
        return self.get_visible_element(self.HEADER_TEXT).text.lower().strip()

    def type_to_normal_input(self, text):
        self.type_text(self.NORMAL_INPUT, text)

    def type_to_validation_input(self, text):
        self.type_text(self.VALIDATION_INPUT, text)

    def get_normal_input_text(self):
        return self.get_visible_element(self.NORMAL_INPUT).text

    def get_disabled_input_text(self):
        return self.get_visible_element(self.DISABLED_INPUT).text

    def is_normal_input_enabled(self):
        return (
            self.get_visible_element(self.NORMAL_INPUT).get_attribute("enabled")
            == "true"
        )

    def is_validation_input_enabled(self):
        return (
            self.get_visible_element(self.VALIDATION_INPUT).get_attribute("enabled")
            == "true"
        )

    def is_disabled_input_enabled(self):
        return (
            self.get_visible_element(self.DISABLED_INPUT).get_attribute("enabled")
            == "true"
        )

    def click_enabled_switch(self):
        self.click(self.ENABLED_SWITCH)

    def is_too_short_text_displayed(self):
        return self.is_displayed(self.TOO_SHORT_TEXT)

    def get_text_length(self):
        return self.get_visible_element(self.TEXT_LENGTH).text
