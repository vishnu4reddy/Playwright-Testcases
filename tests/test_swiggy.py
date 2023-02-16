from playwright.sync_api import Page, expect
import time


def test_example(page: Page) -> None:
    page.goto("https://www.google.com/")
    page.get_by_role("combobox", name="Search").click()
    page.get_by_role("combobox", name="Search").fill("Swiggy")
    page.keyboard.press("Enter")
    page.locator("//h3[normalize-space()='Swiggy']").click()
    # page.locator(
    #     "//a[@href='https://www.swiggy.com/']").get_by_role('heading', name='Swiggy').press('Enter')
    # time.sleep(30)
    # page.locator("//*[@id="root"]/div[1]/div[1]/div/div[1]/div[1]/div/div[1]/div/a[1]").click()
# https://www.swiggy.com/
