from playwright.sync_api import Page
import time
# import re


def test_example(page: Page):
    # Can be "msedge", "chrome-beta", "msedge-beta", "msedge-dev", etc.
    # browser = page.chromium.launch(channel="chrome")
    page.goto("https://www.python.org/")
    time.sleep(3)
    page.get_by_role("menubar", name="main navigation").get_by_role(
        "link", name="Documentation").click()
    # page.get_by_role("link", name="Documentation").click()
    page.get_by_role("link", name="python Docs").click()
    page.get_by_role("link", name="Tutorial").click()
    page.get_by_role("link", name="4.7. Defining Functions").click()
    time.sleep(3)
    # browser.close()
