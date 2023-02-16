from playwright.sync_api import Page, expect
import time 


def test_example(page: Page):

    page.goto("https://www.google.com/")
    page.get_by_role("combobox", name="Search").click()
    page.get_by_role("combobox", name="Search").fill("google")
    page.keyboard.press("Enter")
    page.keyboard.press("End")
    time.sleep(9)
    # page.keyboard.press("arrow")
