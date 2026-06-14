from appium.webdriver.common.appiumby import AppiumBy


from pages.base import BasePage
from utils.get_color import get_element_center_rgb_color


class BgColorPage(BasePage):
    HEADER_TEXT = (AppiumBy.XPATH, '//android.widget.TextView[@text="Background demo"]')
    RED_HALF_BANNER = (
        AppiumBy.XPATH,
        "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[1]",
    )
    BLUE_HALF_BANNER = (
        AppiumBy.XPATH,
        "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]",
    )

    def get_header_text(self):
        return self.get_visible_element(self.HEADER_TEXT).text.lower().strip()

    def get_red_half_banner_color(self, screenshot_dir):
        element = self.get_visible_element(self.RED_HALF_BANNER)

        return get_element_center_rgb_color(
            element=element,
            screenshot_dir=screenshot_dir,
            filename="red_half_banner.png",
        )

    def get_blue_half_banner_color(self, screenshot_dir):
        element = self.get_visible_element(self.BLUE_HALF_BANNER)

        return get_element_center_rgb_color(
            element=element,
            screenshot_dir=screenshot_dir,
            filename="blue_half_banner.png",
        )
