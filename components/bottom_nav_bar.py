from appium.webdriver.common.appiumby import AppiumBy

from pages.base import BasePage


class BottomNavBar(BasePage):
    DP_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "dp")
    DP_BUTTON_TEXT = (
        AppiumBy.ID,
        "com.example.layout_android:id/navigation_bar_item_large_label_view",
    )
    TEXT_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Text")
    TEXT_BUTTON_TEXT = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@resource-id="com.example.layout_android:id/navigation_bar_item_small_label_view" and @text="Text"]',
    )

    def dp_button_is_displayed(self):
        return self.is_displayed(self.DP_BUTTON)

    def get_dp_button_text(self):
        return self.find(self.DP_BUTTON_TEXT).text.lower().strip()

    def text_button_is_displayed(self):
        return self.is_displayed(self.TEXT_BUTTON)

    def get_text_button_text(self):
        return self.find(self.TEXT_BUTTON_TEXT).text.lower().strip()
