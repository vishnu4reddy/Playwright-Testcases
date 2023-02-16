import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture()
def page_1():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, channel="msedge")
        # Can be "msedge", "chrome-beta", "msedge-beta", "msedge-dev", etc.
        # browser = p.chromium.launch(channel="msedge")
        page = browser.new_page()
        yield page
