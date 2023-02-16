from playwright.sync_api import Page
import time
from Data import imp
name = imp.name
Email = imp.username
password = imp.password


def test_example(page: Page):
    page.goto("https://www.google.com/")
    page.get_by_role("combobox", name="Search").click()
    page.get_by_role("combobox", name="Search").fill("narendramodi")
    page.keyboard.press("Enter")
    page.locator(
        "//h3[contains(text(),'Narendra Modi | NarendraModi.in Official Website o')]").click()
    page.locator("//div[@class='login']//a[1]").click()
    page.get_by_role("link", name="Create New Account").click()
    page.get_by_role("textbox", name="Enter Name").click(button="left")
    page.get_by_role("textbox", name="Enter Name").fill(name)
    page.get_by_role("textbox", name="Enter Email").click(button="left")
    page.get_by_role("textbox", name="Enter Email").fill(Email)
    page.get_by_role("textbox", name="Enter Password").click(button="left")
    page.get_by_role("textbox", name="Enter Password").fill(password)
    page.get_by_role("textbox", name="Enter Confirm Password").click(
        button="left")
    page.get_by_role("textbox", name="Enter Confirm Password").fill(password)
    time.sleep(3)
    # page.locator("").click()
    # page.frame_locator("iframe[name=\"a-owzg5w9an80m\"]").get_by_role("checkbox", name="I'm not a robot").click()
    page.frame_locator("//iframe[@title='reCAPTCHA']").get_by_role("checkbox", name="I'm not a robot").click()
    page.locator("//li[14]//input[1]").check()
    page.get_by_role("button", name="Sign Up").click(button="left")
    time.sleep(10)
