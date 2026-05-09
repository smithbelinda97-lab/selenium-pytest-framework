from selenium.webdriver.common.by import By


def get_element(driver, locators, page, element):

    # Fetch locator details from JSON
    locator = locators[page][element]

    # Map locator types to Selenium By methods
    by_map = {
        "id": By.ID,
        "css": By.CSS_SELECTOR,
        "xpath": By.XPATH,
        "name": By.NAME,
        "class": By.CLASS_NAME,
        "tag": By.TAG_NAME,
        "link_text": By.LINK_TEXT,
        "partial_link_text": By.PARTIAL_LINK_TEXT
    }

    # Return the web element
    return driver.find_element(
        by_map[locator["by"]],
        locator["value"]
    )