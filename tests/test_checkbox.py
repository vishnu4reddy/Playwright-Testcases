from playwright.sync_api import Page, expect
import time
# import re


def test_example(page: Page) -> None:
    page.goto("https://www.ironspider.ca/forms/checkradio.htm")
    # Check the heckbox
    page.locator("//input[@value='red']").check()
    time.sleep(3)
    page.goto(
        "https://www.keynotesupport.com/internet/web-contact-form-example-radio-buttons.shtml")
    time.sleep(3)
    page.locator("//input[@value='QBP']").check()
    time.sleep(3)
