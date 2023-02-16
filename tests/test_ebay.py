from playwright.sync_api import Page, expect
import time
from Data import imp
from playwright.sync_api import sync_playwright



mobile_no = imp.mobile_no
password = imp.password


def test_example(page:Page):

        page.goto("https://www.google.com/")
        page.get_by_role("combobox", name="Search").click()
        page.get_by_role("combobox", name="Search").fill("ebay.in")
        page.keyboard.press("Enter")
        page.locator("//h3[normalize-space()='Sign in or Register | eBay']").click()
        page.locator("//body").click()
        # page.locator("//a[@id='create-account-link']").click()
        time.sleep(5)

