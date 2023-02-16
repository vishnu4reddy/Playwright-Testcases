from playwright.sync_api import Page, expect
import time
from Data import imp
Email = imp.username
password = imp.password


def share(page: Page):
    page.goto("https://www.google.com/")
    page.get_by_role("combobox", name="Search").click()
    page.get_by_role("combobox", name="Search").fill("Rolex")
    page.keyboard.press("Enter")
    page.locator(
        "//h3[normalize-space()='Official Rolex Website - Swiss Luxury Watches']").click()
    with page.expect_popup() as page1_info:
        page.get_by_role(
            "button", name="Share this page on Linkedin New tab").click()
    page1 = page1_info.value
    page1.get_by_label("Email or Phone").click()
    page1.get_by_label("Email or Phone").fill("9490058514")
    page1.get_by_label("Password").click()
    page1.get_by_label("Password").fill("vishnu161999")
    page1.locator("#organic-div form").get_by_role("button",
                                                   name="Sign in").click()
    page1.get_by_role("button", name="Share in a post").click()
    page1.locator("#ember53").click()
    with page1.expect_popup() as page2_info:
        page1.get_by_role("link", name="Continue to LinkedIn").click()
    page2 = page2_info.value
    page2.get_by_role("button", name="vishnu vardhan reddy usirike Me").click()
    page2.get_by_role("link", name="Sign Out").click()
