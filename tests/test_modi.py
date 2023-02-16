from playwright.sync_api import Page
import time
from Data import imp
name = imp.name
Email = imp.username
password = imp.password
mobile_no = imp.mobile_no


def test_example(page: Page):
    page.goto("https://www.google.com/")
    page.get_by_role("combobox", name="Search").click()
    page.get_by_role("combobox", name="Search").fill("narendramodi")
    page.keyboard.press("Enter")
    page.locator(
        "//h3[contains(text(),'Narendra Modi | NarendraModi.in Official Website o')]").click()
    page.locator("//div[@class='login']//a[1]").click()
    page.locator("//input[@id='email_address']").click()
    page.locator("//input[@id='email_address']").fill(Email)
    page.locator("//input[@id='password']").click()
    page.locator("//input[@id='password']").fill(password)
    page.keyboard.press("Enter")
    print(page.url)
    # page.get_by_role("button", name="LOGIN").click()
    page.goto("https://auth.mygov.in/user/login?destination=oauth2/authorize")
    page.get_by_role("link", name="Register Now").click()
    page.locator("//input[@id='edit-full-name']").fill(name)
    page.keyboard.press("Tab")
    page.locator("//input[@id='edit-email']").fill(Email)
    page.keyboard.press("Tab")  # selecting India
    page.keyboard.press("Tab")   # going to next
    page.locator("//input[@id='edit-number']").fill(mobile_no)
    page.keyboard.press("Tab")
    for i in range(16):
        page.keyboard.press("ArrowDown")
    time.sleep(3)
    page.keyboard.press("Tab")
    for i in range(9):
        page.keyboard.press("ArrowDown")
    time.sleep(3)
    page.keyboard.press("Tab")
    for i in range(25):
        page.keyboard.press("ArrowDown")
    time.sleep(3)
    page.keyboard.press("Tab")
    # page.keyboard.press("Tab")
    for i in range(1):
        page.keyboard.press("ArrowDown")
    time.sleep(3)
    page.keyboard.press("Tab")
    page.keyboard.press("Tab")
    page.keyboard.press("Enter")
    # Page.locator'dropdown'.click()
    # page.get_by_role("combobox", name="Please select date").select_option("16")
    # page.get_by_role("combobox", name="Please select month").select_option("September")
    # page.get_by_role("combobox", name="Please select year").select_option("1999")
    # page.get_by_role("combobox", name="Please coose your Gender").select_option("male")
    # page.keyboard.press("Tab")
    # page.keyboard.press("Tab")
    # page.keyboard.press("Enter")
    # page.get_by_role("checkbox", name="Have a referral code?").check()
    # page.get_by_role("button", name="Create New Account").click()
    # # time.sleep(10)
    # page.locator("//input[@id='edit-name']").fill(Email)
    # page.locator("//input[@id='edit-pass']").fill(password)
    # page.locator("//input[@id='edit-submit']").click()
    # # page.keyboard.press("Enter")

    # time.sleep(10)



# import pytest
# from playwright.sync_api import sync_playwright


# class Settings:
#     name = 'Parthiban'

# @pytest.fixture
# def page(request):
#     class just:
#         def __init__(self, page, request):
#             self.page = page
#             self.settings = request.config.settings
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)
#         page = browser.new_page()
#         yield just(page, request)
#         page.close()

# def pytest_configure(config):
#     print(config.getoption('--base-url'))
#     config.settings = Settings
