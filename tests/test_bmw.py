from playwright.sync_api import Page
import time


def test_example(page: Page):
    page.goto("https://www.google.com/")
    page.get_by_role("combobox", name="Search").click()
    page.get_by_role("combobox", name="Search").fill("bmw.in")
    page.keyboard.press("Enter")
    page.get_by_role("heading", name="BMW India").click()
    page.get_by_role("link", name="Models").click()
    page.locator(
        "//button[@title='The new BMW 3 Series Gran Limousine']").click(button="left")
    time.sleep(5)
