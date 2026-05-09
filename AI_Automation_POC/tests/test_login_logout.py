from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import json
import os
import sys
import time


# ----------------------------------------
# Add Helper Folder to Python Path
# ----------------------------------------
sys.path.append("../helpers")


# ----------------------------------------
# Import Helper Files
# ----------------------------------------
from locator_helper import get_element
from screenshot_helper import take_screenshot
from report_helper import (
    add_screenshot_to_report,
    save_report
)


# ----------------------------------------
# Load Locator JSON
# ----------------------------------------
with open("../locators/locators.json") as f:
    locators = json.load(f)


# ----------------------------------------
# Setup Chrome Driver
# ----------------------------------------
service = Service("../drivers/chromedriver.exe")

driver = webdriver.Chrome(service=service)

driver.maximize_window()


# ----------------------------------------
# Explicit Wait
# ----------------------------------------
wait = WebDriverWait(driver, 10)


try:

    # ========================================
    # Step 1 - Launch SauceDemo Application
    # ========================================
    driver.get("https://www.saucedemo.com/")

    screenshot = take_screenshot(
        driver,
        "01_Application_Launch"
    )

    add_screenshot_to_report(
        "Application Launch",
        screenshot
    )


    # ========================================
    # Step 2 - Enter Username
    # ========================================
    username = get_element(
        driver,
        locators,
        "login_page",
        "username_input"
    )

    username.send_keys("standard_user")

    screenshot = take_screenshot(
        driver,
        "02_Username_Entered"
    )

    add_screenshot_to_report(
        "Username Entered",
        screenshot
    )


    # ========================================
    # Step 3 - Enter Password
    # ========================================
    password = get_element(
        driver,
        locators,
        "login_page",
        "password_input"
    )

    password.send_keys("secret_sauce")

    screenshot = take_screenshot(
        driver,
        "03_Password_Entered"
    )

    add_screenshot_to_report(
        "Password Entered",
        screenshot
    )


    # ========================================
    # Step 4 - Click Login Button
    # ========================================
    login_button = get_element(
        driver,
        locators,
        "login_page",
        "login_button"
    )

    login_button.click()


    # ========================================
    # Step 5 - Validate Login
    # ========================================
    wait.until(
        EC.url_contains("inventory")
    )

    assert "inventory" in driver.current_url

    print("Login successful")

    screenshot = take_screenshot(
        driver,
        "04_Login_Successful"
    )

    add_screenshot_to_report(
        "Login Successful",
        screenshot
    )


    # ========================================
    # Step 6 - Open Hamburger Menu
    # ========================================
    menu_button = wait.until(
        lambda d: get_element(
            d,
            locators,
            "home_page",
            "menu_button"
        )
    )

    menu_button.click()
    wait = WebDriverWait(driver, 10)
    screenshot = take_screenshot(
        driver,
        "05_Menu_Opened"
    )

    add_screenshot_to_report(
        "Menu Opened",
        screenshot
    )


    # ========================================
    # Step 7 - Click Logout
    # ========================================
    logout_link = wait.until(
        lambda d: get_element(
            d,
            locators,
            "home_page",
            "logout_link"
        )
    )

    logout_link.click()


    # ========================================
    # Step 8 - Validate Logout
    # ========================================
    wait.until(
        EC.url_to_be(
            "https://www.saucedemo.com/"
        )
    )

    assert "saucedemo" in driver.current_url

    print("Logout successful")

    screenshot = take_screenshot(
        driver,
        "06_Logout_Successful"
    )

    add_screenshot_to_report(
        "Logout Successful",
        screenshot
    )


    # ========================================
    # Step 9 - Save Execution Report
    # ========================================
    if not os.path.exists("../reports"):
        os.makedirs("../reports")

    report_path = (
        "../reports/"
        "SauceDemo_Execution_Report.docx"
    )

    save_report(report_path)


except Exception as e:

    print(f"Test Failed: {e}")

    screenshot = take_screenshot(
        driver,
        "Error_Screenshot"
    )

    add_screenshot_to_report(
        "Test Failure",
        screenshot
    )

    save_report(
        "../reports/Failure_Report.docx"
    )


finally:

    time.sleep(3)

    driver.quit()

    print("Browser closed successfully")