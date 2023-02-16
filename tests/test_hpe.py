from playwright.sync_api import Page
import time
from Data import imp
Email = imp.username
password = imp.password
first_name = imp.first_name
last_name = imp.last_name


def test_example(page: Page):
    page.goto("https://www.google.com/")
    page.get_by_role("combobox", name="Search").click()
    page.get_by_role("combobox", name="Search").fill(
        "hewlett packard enterprise")
    page.keyboard.press("Enter")
    page.locator(
        "//h3[normalize-space()='Hewlett Packard Enterprise (HPE) | India']").click()
    time.sleep(5)
    page.locator("//span[@class='gn-account-btn-text']").click()
    # time.sleep(5)
    # page.get_by_role("link", name="Create an account").click()
    page.locator(".btn-typo4.rounded.secondary.green.small").click()
    page.locator("//input[@id='email-address']").click()
    page.locator("//input[@id='email-address']").fill(Email)
    page.keyboard.press("Tab")
    # page.pause()
    page.locator("//input[@id='new-password']").fill(password)
    time.sleep(2)
    page.keyboard.press("Tab")
    time.sleep(2)
    page.keyboard.type(password)
    page.locator("//input[@id='confirm-password']").fill(password)
    time.sleep(2)
    page.keyboard.press("Tab")
    time.sleep(2)
    page.locator("//input[@id='first-name']").fill(first_name)
    time.sleep(2)
    page.keyboard.press("Tab")
    time.sleep(2)
    page.locator("//input[@id='last-name']").fill(last_name)
    time.sleep(2)
    page.keyboard.press("Tab")
    time.sleep(2)
    page.keyboard.press("ArrowDown")
    time.sleep(2)
    page.keyboard.press("i")
    time.sleep(2)
    page.keyboard.press("ArrowDown")
    time.sleep(2)
    page.keyboard.press("Enter")
    time.sleep(2)
    page.locator("#ac-v2-accept").check()
    time.sleep(2)
    for i in range(3):
        page.keyboard.press("Enter")
        time.sleep(2)
    page.keyboard.press("Tab")
    time.sleep(2)
    page.locator("//input[@id='email-opt-in']").check()
    time.sleep(2)
    page.keyboard.press("Tab")
    time.sleep(2)
    page.keyboard.press("Enter")        
    time.sleep(9)
