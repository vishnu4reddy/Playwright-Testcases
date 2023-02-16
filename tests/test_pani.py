from playwright.sync_api import Page
import time 


def test_example(page: Page) -> None:
    page.goto("https://www.google.com/")
    page.get_by_role("combobox", name="Search").click()
    page.get_by_role("combobox", name="Search").fill(
        "Panimalar Engineering College")
    page.keyboard.press("Enter")
    page.mouse.up()
    page.mouse.down()
    page.mouse.up()
    page.mouse.down()
    time.sleep(5)
    page.mouse.click(1000, 1000)
    time.sleep(5)
    # page.get_by_role("heading", name="Panimalar Engineering College").click()

# from playwright.sync_api import sync_playwright

# def run(playwright):
#     iphone_12 = playwright.devices['iPhone 12']
#     browser = playwright.webkit.launch(headless=False)
#     context = browser.new_context(
#         **iphone_12,
#     )

# with sync_playwright() as playwright:
#     run(playwright)
