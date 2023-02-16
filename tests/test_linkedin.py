from playwright.sync_api import Page
from Data import imp


mobile_no = imp.mobile_no
password = imp.password


def test_example(page: Page):

    page.goto("https://www.google.com/")
    page.get_by_role("combobox", name="Search").click()
    page.get_by_role("combobox", name="Search").fill("Linkedin")
    page.keyboard.press("Enter")
    page.get_by_role("link", name="Login").click()
    page.screenshot(
        path="D:\\Workspace\\Practice\\Playwright Testcases\\screenshot\\screenshot.png", full_page=True)
    # time.sleep(10)
    page.get_by_role("textbox", name="Email or Phone").fill(mobile_no)
    page.get_by_role("textbox", name="Password").fill(password)
    page.locator("//button[@aria-label='Sign in']").click()
    page.screenshot(path="screenshot.png", full_page=True)
    # page.get_by_role("img", name="vishnu vardhan reddy usirike").click()
    page.locator("//body").click()
    # context.close()
