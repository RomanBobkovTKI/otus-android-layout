from pathlib import Path

from PIL import Image


def get_element_center_rgb_color(
    element, screenshot_dir: Path, filename: str
) -> tuple[int, int, int]:
    screenshot_path = screenshot_dir / filename

    element.screenshot(str(screenshot_path))

    image = Image.open(screenshot_path)

    width, height = image.size
    center_x = width // 2
    center_y = height // 2

    pixel = image.getpixel((center_x, center_y))

    return pixel[:3]
