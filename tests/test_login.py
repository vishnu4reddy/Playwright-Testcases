from playwright.sync_api import Page, expect
import time


def test_example(page: Page) :
    page.goto("https://www.google.com/")
    page.get_by_role("combobox", name="Search").click()
    page.get_by_role("combobox", name="Search").fill("linkedin")
    # page.get_by_role("button").press("Enter")
    page.keyboard.press("Enter")
    time.sleep(3)
    page.close()


