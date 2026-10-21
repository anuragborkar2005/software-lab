"""
Automated UI Testing Script for Login Functionality
Target Application: https://the-internet.herokuapp.com/login
Tool: Selenium WebDriver with Python
"""

import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_driver(headless=True):
    """Initialize and configure Chrome WebDriver."""
    options = Options()
    if headless:
        options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    
    # In standard local environments with Chrome installed:
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    return driver


def test_login_success(driver=None):
    """Test Case 1: Valid Login Credentials (Happy Path)"""
    print("\n" + "=" * 65)
    print("RUNNING TEST CASE 1: Valid Login Authentication (Success Path)")
    print("=" * 65)
    
    close_driver_after = False
    if driver is None:
        driver = get_driver()
        close_driver_after = True

    try:
        url = "https://the-internet.herokuapp.com/login"
        print(f"[Step 1] Navigating to URL: {url}")
        driver.get(url)

        print("[Step 2] Locating username and password input fields...")
        username_field = driver.find_element(By.ID, "username")
        password_field = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

        print("[Step 3] Entering valid credentials ('tomsmith' / 'SuperSecretPassword!')...")
        username_field.clear()
        username_field.send_keys("tomsmith")
        password_field.clear()
        password_field.send_keys("SuperSecretPassword!")

        print("[Step 4] Clicking Login button...")
        login_button.click()

        print("[Step 5] Waiting for flash notification banner...")
        flash_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "flash"))
        )
        flash_text = flash_element.text.strip()
        print(f"[Step 6] Captured Flash Alert Text:\n         --> \"{flash_text}\"")

        # Assertions
        assert "You logged into a secure area!" in flash_text, (
            f"Assertion Failed: Expected success message not found. Got: {flash_text}"
        )
        assert "/secure" in driver.current_url, (
            f"Assertion Failed: Expected redirect to /secure. Current URL: {driver.current_url}"
        )
        print("[RESULT] >> TEST CASE 1 PASSED: Successfully authenticated into secure area!")

    finally:
        if close_driver_after and driver:
            driver.quit()


def test_login_failure(driver=None):
    """Test Case 2: Invalid Login Credentials (Failure Path)"""
    print("\n" + "=" * 65)
    print("RUNNING TEST CASE 2: Invalid Login Password (Failure Path)")
    print("=" * 65)

    close_driver_after = False
    if driver is None:
        driver = get_driver()
        close_driver_after = True

    try:
        url = "https://the-internet.herokuapp.com/login"
        print(f"[Step 1] Navigating to URL: {url}")
        driver.get(url)

        print("[Step 2] Locating username and password input fields...")
        username_field = driver.find_element(By.ID, "username")
        password_field = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

        print("[Step 3] Entering invalid credentials ('tomsmith' / 'WrongPassword123!')...")
        username_field.clear()
        username_field.send_keys("tomsmith")
        password_field.clear()
        password_field.send_keys("WrongPassword123!")

        print("[Step 4] Clicking Login button...")
        login_button.click()

        print("[Step 5] Waiting for flash alert banner...")
        flash_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "flash"))
        )
        flash_text = flash_element.text.strip()
        print(f"[Step 6] Captured Flash Alert Text:\n         --> \"{flash_text}\"")

        # Assertions
        assert "Your password is invalid!" in flash_text, (
            f"Assertion Failed: Expected invalid password message. Got: {flash_text}"
        )
        assert "/login" in driver.current_url, (
            f"Assertion Failed: Expected to remain on /login. Current URL: {driver.current_url}"
        )
        print("[RESULT] >> TEST CASE 2 PASSED: Successfully intercepted invalid login attempt!")

    finally:
        if close_driver_after and driver:
            driver.quit()


if __name__ == "__main__":
    try:
        test_login_success()
        test_login_failure()
        print("\n" + "=" * 65)
        print("ALL AUTOMATED UI TEST SUITES EXECUTED SUCCESSFULLY.")
        print("=" * 65)
    except Exception as exc:
        print(f"\n[ERROR] Test Execution Failed: {exc}", file=sys.stderr)
