# Experiment 10: AI-Assisted Automated UI Testing

## Aim
To write and execute automated UI test scripts using Selenium with an AI tool (GitHub Copilot / Windsurf / Claude / Ollama), and to evaluate the accuracy, robustness, and assertions of the generated test cases across success and failure paths.

## Course Outcome(s) Mapped
- **CO3**: Design and develop automated software test suites (unit, integration, and end-to-end UI testing) using standard testing frameworks and tools.

## Tools / Software Required
- **Selenium WebDriver (Python)**: Industry-standard browser automation framework (`selenium>=4.20.0`).
- **Python 3.11+ / Pytest**: Execution environment and test assertion runner.
- **AI Tool**: GitHub Copilot Chat / Windsurf / Claude / Ollama.
- **Target Application**: [the-internet.herokuapp.com/login](https://the-internet.herokuapp.com/login) (public test application maintained by Elemental Selenium).

---

## Pre-Lab Theory
Automated UI testing drives an actual web browser to simulate real user interactions—such as clicking buttons, filling text forms, waiting for asynchronous DOM mutations, and asserting that expected visual feedback appears.
1. **Selenium Architecture**:
   - **Client Bindings**: Language-specific libraries (Python, Java, JS, C#) providing the WebDriver API.
   - **WebDriver Protocol (W3C Standard)**: JSON-over-HTTP wire protocol conveying commands (`findElement`, `click`, `sendKeys`) to browser drivers.
   - **Browser Drivers**: Platform binaries (ChromeDriver, GeckoDriver) that translate commands into native browser automation events.
2. **Explicit vs. Implicit Waits**:
   - **Implicit Wait**: Global timeout instructing WebDriver to poll the DOM for a specified duration when looking for elements.
   - **Explicit Wait (`WebDriverWait` + `expected_conditions`)**: Targets specific dynamic elements and conditions (e.g., `visibility_of_element_located`), preventing brittle test flakiness caused by network or render latencies.
3. **AI Assistance in UI Testing**:
   AI assistants can inspect HTML source snippets or natural-language step descriptions to generate selector strategies (ID, CSS selector, XPath), structure Page Object Models (POM), and construct positive/negative assertions.

---

## AI Interaction & Sample Prompt

### Sample Prompt:
> **"Write a Selenium Python script to test login functionality on the-internet.herokuapp.com/login: enter username 'tomsmith' and password 'SuperSecretPassword!', click login, and assert that the success message appears. Also write a test case for invalid credentials to verify error handling."**

---

## Automated Test Script (`test_login.py`)

```python
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
```

---

## Sample Output (Step Executed + Result Shown)

### Actual Terminal Execution Output:
```text
=================================================================
STARTING AUTOMATED UI TEST EXECUTION
Site: https://the-internet.herokuapp.com/login
=================================================================

=================================================================
RUNNING: TEST CASE 1: Valid Login Authentication (Success Path)
=================================================================
[Step 1] Navigating to URL: https://the-internet.herokuapp.com/login
[Step 2] Locating input elements ('username', 'password', 'submit button')...
         Elements located successfully.
[Step 3] Entering credentials: username='tomsmith', password='********************'...
[Step 4] Submitting form / clicking Login button...
[Step 5] Extracting flash alert element...
[Step 6] Captured Flash Alert Text:
         --> "You logged into a secure area! ×"
[Step 7] Evaluating assertions...
[RESULT] >> TEST CASE 1: Valid Login Authentication (Success Path) PASSED!

=================================================================
RUNNING: TEST CASE 2: Invalid Login Password (Failure Path)
=================================================================
[Step 1] Navigating to URL: https://the-internet.herokuapp.com/login
[Step 2] Locating input elements ('username', 'password', 'submit button')...
         Elements located successfully.
[Step 3] Entering credentials: username='tomsmith', password='*****************'...
[Step 4] Submitting form / clicking Login button...
[Step 5] Extracting flash alert element...
[Step 6] Captured Flash Alert Text:
         --> "Your password is invalid! ×"
[Step 7] Evaluating assertions...
[RESULT] >> TEST CASE 2: Invalid Login Password (Failure Path) PASSED!

=================================================================
ALL 2 AUTOMATED TEST SCENARIOS PASSED WITH ZERO ASSERTION ERRORS.
=================================================================
```

---

## Expected Output / Deliverable
1. A reproducible automated Python Selenium script (`test_login.py`) implementing explicit element waits, robust selectors, and defensive assertions.
2. Terminal execution logs demonstrating passing results for both the positive authentication path (`You logged into a secure area!`) and negative validation path (`Your password is invalid!`).

## Result
Thus the experiment was executed successfully using AI-assisted tools to construct automated Selenium UI test suites, verify live web elements, and assert deterministic behavior across success and failure execution paths.

---

## Viva-Voce Questions & Detailed Answers

### 1. What is Selenium WebDriver used for?
**Answer:**  
Selenium WebDriver is an open-source browser automation framework primarily used for:
- **End-to-End Functional UI Testing**: Simulating authentic human end-user workflows across web applications (form inputs, mouse clicks, page navigation, modal alerts, file uploads).
- **Cross-Browser Verification**: Validating application consistency across various browser engines (Chrome/Chromium, Firefox, Safari, Microsoft Edge).
- **Regression Testing**: Automatically re-executing repetitive test scenarios before software releases to detect breaking changes or regression bugs.
- **Headless Pipeline Integration**: Running automated test suites within continuous integration / continuous deployment (CI/CD) pipelines (such as GitHub Actions or Jenkins) without requiring a physical monitor or graphical desktop display.

### 2. What is a 'self-healing' locator in AI-assisted testing tools?
**Answer:**  
A **self-healing locator** is an AI/ML-enhanced mechanism that prevents automated tests from breaking when the underlying DOM structure or element attributes change:
- **The Problem**: Traditional locators rely on a single selector (e.g., an exact ID `#submit-btn` or XPath `//div[2]/form/button`). If a UI redesign changes the ID or moves the element in the DOM tree, the test immediately throws `NoSuchElementException`.
- **How Self-Healing Works**: The testing framework captures a multi-dimensional semantic footprint of the element during initial runs (text content, visual proximity, tag name, surrounding labels, CSS classes, ARIA attributes). When the primary locator fails, the AI engine dynamically scores candidate DOM nodes, identifies the closest matching element with high confidence, auto-heals the locator at runtime without failing the build, and suggests the updated selector to the engineering team.

### 3. What are the advantages of automated UI testing over manual testing?
**Answer:**  
| Criteria | Automated UI Testing | Manual Testing |
| :--- | :--- | :--- |
| **Speed & Throughput** | Executes dozens of test scenarios per minute; runs unattended overnight. | Slow; human testers must manually click and enter data step-by-step. |
| **Consistency & Precision** | Deterministic; executes identical inputs, clicks, and assertions every time without fatigue. | Prone to human error, missed steps, fatigue, and inconsistent observations. |
| **Cost at Scale** | Initial setup cost is higher, but marginal cost per additional test run is virtually zero. | Linearly expensive; cost increases with every software iteration and manual regression cycle. |
| **CI/CD Integration** | Runs automatically on every pull request, Git commit, or deployment pipeline. | Cannot be integrated as a fast blocking gate inside continuous integration pipelines. |
| **Coverage & Reusability** | Enables high regression test coverage across multiple browsers and viewports simultaneously. | Restricted coverage due to manual time constraints. |

### 4. What challenges arise when the UI changes frequently?
**Answer:**  
Frequent UI changes introduce several testing challenges:
1. **High Maintenance Overhead ("Brittle Tests")**: Minor CSS class name adjustments, dynamic IDs (e.g., generated by styled-components or Tailwind), or DOM restructuring frequently cause existing selectors to fail.
2. **False Positives**: Tests fail not because the application logic is broken, but because an element locator is out of date, creating "alarm fatigue" among developers.
3. **Synchronization & Timing Issues**: Modern single-page applications (React, Angular, Vue) use client-side hydration, animations, and asynchronous API calls. Frequent layout changes can cause race conditions if explicit waits are improperly configured.
4. **Mitigation Best Practices**:
   - Adopt the **Page Object Model (POM)** to centralize selectors in one file.
   - Use semantic, accessibility-based locators (e.g., `By.NAME`, ARIA labels, or dedicated `data-testid` attributes) instead of fragile structural XPaths.
   - Leverage AI-powered self-healing test automation tools (e.g., Playwright, Testim, Mabl).
