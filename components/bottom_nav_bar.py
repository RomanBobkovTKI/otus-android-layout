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
    BG_COLOR_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "bg_color")
    BG_COLOR_BUTTON_TEXT = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@resource-id="com.example.layout_android:id/navigation_bar_item_small_label_view" and @text="bg_color"]',
    )
    INPUTS_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "inputs")
    INPUTS_BUTTON_TEXT = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@resource-id="com.example.layout_android:id/navigation_bar_item_small_label_view" and @text="inputs"]',
    )

    def dp_button_is_displayed(self):
        return self.is_displayed(self.DP_BUTTON)

    def get_dp_button_text(self):
        return self.get_visible_element(self.DP_BUTTON_TEXT).text.lower().strip()

    def text_button_is_displayed(self):
        return self.is_displayed(self.TEXT_BUTTON)

    def get_text_button_text(self):
        return self.get_visible_element(self.TEXT_BUTTON_TEXT).text.lower().strip()

    def bg_color_button_is_displayed(self):
        return self.is_displayed(self.BG_COLOR_BUTTON)

    def bg_color_button_text(self):
        return self.get_visible_element(self.BG_COLOR_BUTTON_TEXT).text.lower().strip()

    def inputs_button_is_displayed(self):
        return self.is_displayed(self.INPUTS_BUTTON)

    def get_inputs_button_text(self):
        return self.get_visible_element(self.INPUTS_BUTTON_TEXT).text.lower().strip()
