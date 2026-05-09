import os

SCREENSHOT_FOLDER = "screenshots"

if not os.path.exists(SCREENSHOT_FOLDER):
    os.makedirs(SCREENSHOT_FOLDER)


def take_screenshot(driver, step_name):

    screenshot_path = os.path.join(
        SCREENSHOT_FOLDER,
        f"{step_name}.png"
    )

    driver.save_screenshot(screenshot_path)

    print(f"Screenshot saved: {screenshot_path}")

    return screenshot_path