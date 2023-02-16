from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://www.google.com/")
    page.get_by_role("combobox", name="Search").click()
    page.get_by_role("combobox", name="Search").fill("penguin")
    page.get_by_role("combobox", name="Search").press("Enter")
    page.locator("#hdtb-msb").get_by_role("link", name="Images").click()
    page.get_by_role("button", name="King Penguin | Facts, pictures & more about King Penguin").click()
    page.screenshot(path='penguinimage.png')