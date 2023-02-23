from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.w3schools.com/")
    page.get_by_role("link", name="Learn HTML").click()
    page.locator("#leftmenuinnerinner").get_by_role("link", name="HTML Elements").click()
    with page.expect_popup() as page1_info:
        page.get_by_role("link", name="Try it Yourself »").nth(2).click()
    page = page1_info.value

    # ---------------------
    context.close()
    browser.close()
