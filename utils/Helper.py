import time
from selenium.webdriver.common.by import By

def highlight(element, driver, duration=0.3):
    """
    Highlights (blinks) a Selenium WebDriver element by applying a temporary border.
    :param element: The WebElement to highlight.
    :param driver: The WebDriver instance.
    :param duration: The time (in seconds) to keep the element highlighted.
    """
    original_style = element.get_attribute("style")

    # Use JavaScript to apply a visible border and background
    driver.execute_script(
        "arguments[0].setAttribute('style', arguments[1]);",
        element,
        "border: 4px solid blue; border-style: dashed;"
    )

    if duration > 0:
        time.sleep(duration)
        # Revert the style back to the original
        driver.execute_script(
            "arguments[0].setAttribute('style', arguments[1]);",
            element,
            original_style
        )