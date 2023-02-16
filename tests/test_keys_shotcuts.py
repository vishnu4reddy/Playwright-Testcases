from playwright.sync_api import Page, expect
import time
# import re Welcome to Python.org


def test_example(page: Page) -> None:
    page.goto("https://www.google.co.in/")
    time.sleep(3)
    page.get_by_role("combobox", name="Search").fill("python")
    page.get_by_role("button", name="Google Search").press("Enter")
    page.get_by_role("heading", name="Welcome to Python.org").click()
    page.get_by_role("link", name="docs.python.org").click(button="left")
    # time.sleep(3)
    # page.get_by_placeholder("textbox").click()
    # page.get_by_role("textbox", name="Quick search").fill("Class and Object")
    # page.get_by_role("button", name="Go").click()
    
    # page.goto("https://docs.python.org/3/search.html?q=&check_keywords=yes&area=default")
    # page.get_by_role("textbox", name="Search").fill("Class and Object ")


