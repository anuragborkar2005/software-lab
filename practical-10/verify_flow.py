"""
Automated UI Flow Verification Script
Performs session-authenticated end-to-end verification of the login flows
on https://the-internet.herokuapp.com/login.
"""

import urllib.request
import urllib.parse
import http.cookiejar
import re

BASE_URL = "https://the-internet.herokuapp.com"


def execute_login_test(username, password, expected_alert, expected_url_fragment, test_label):
    print("\n" + "=" * 65)
    print(f"RUNNING: {test_label}")
    print("=" * 65)

    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

    # Step 1: GET Login Page
    print(f"[Step 1] Navigating to URL: {BASE_URL}/login")
    resp1 = opener.open(f"{BASE_URL}/login")
    html1 = resp1.read().decode("utf-8")
    assert resp1.status == 200, f"Expected 200 OK, got {resp1.status}"

    print("[Step 2] Locating input elements ('username', 'password', 'submit button')...")
    assert 'name="username"' in html1 and 'id="username"' in html1, "Username field not found"
    assert 'name="password"' in html1 and 'id="password"' in html1, "Password field not found"
    print("         Elements located successfully.")

    # Step 3: POST Form Submission
    print(f"[Step 3] Entering credentials: username='{username}', password='{'*' * len(password)}'...")
    form_data = urllib.parse.urlencode({"username": username, "password": password}).encode("utf-8")
    req = urllib.request.Request(
        f"{BASE_URL}/authenticate",
        data=form_data,
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded"
        }
    )
    print("[Step 4] Submitting form / clicking Login button...")
    resp2 = opener.open(req)
    final_url = resp2.geturl()
    html2 = resp2.read().decode("utf-8")

    # Step 5 & 6: Extract flash message
    print("[Step 5] Extracting flash alert element...")
    flash_match = re.search(r"<div[^>]*id=['\"]flash['\"][^>]*>(.*?)</div>", html2, re.DOTALL)
    assert flash_match, "Flash message element not found in response HTML"
    
    raw_flash = flash_match.group(1)
    # Strip HTML tags and close button
    clean_flash = re.sub(r"<[^>]+>", "", raw_flash).strip()
    # Normalize whitespace
    clean_flash = " ".join(clean_flash.split())
    print(f"[Step 6] Captured Flash Alert Text:\n         --> \"{clean_flash}\"")

    # Assertions
    print("[Step 7] Evaluating assertions...")
    assert expected_alert in clean_flash, (
        f"Assertion Failed! Expected '{expected_alert}', got '{clean_flash}'"
    )
    assert expected_url_fragment in final_url, (
        f"Assertion Failed! Expected '{expected_url_fragment}' in URL, got '{final_url}'"
    )
    print(f"[RESULT] >> {test_label} PASSED!")


if __name__ == "__main__":
    print("=" * 65)
    print("STARTING AUTOMATED UI TEST EXECUTION")
    print("Site: https://the-internet.herokuapp.com/login")
    print("=" * 65)

    # Test Case 1: Success Path
    execute_login_test(
        username="tomsmith",
        password="SuperSecretPassword!",
        expected_alert="You logged into a secure area!",
        expected_url_fragment="/secure",
        test_label="TEST CASE 1: Valid Login Authentication (Success Path)"
    )

    # Test Case 2: Failure Path
    execute_login_test(
        username="tomsmith",
        password="WrongPassword123!",
        expected_alert="Your password is invalid!",
        expected_url_fragment="/login",
        test_label="TEST CASE 2: Invalid Login Password (Failure Path)"
    )

    print("\n" + "=" * 65)
    print("ALL 2 AUTOMATED TEST SCENARIOS PASSED WITH ZERO ASSERTION ERRORS.")
    print("=" * 65)
