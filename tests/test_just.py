from playwright.sync_api import Page, expect

def test_grammerly(page: Page):
    page.goto("https://www.grammarly.com/")
    page.get_by_role("button", name="Why Grammarly").click()
    page.close