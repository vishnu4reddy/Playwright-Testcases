
import time


def test_amazon(page):
    page.goto("https://aws.amazon.com/")
    # locator = page.locator("div")
    # more_than_ten = locator.evaluate_all("(divs, min) => divs.length > min", 10)
    # source = Page.locator("//img[@alt='Amazon Web Services Marketing']")
    # target = Page.locator("//body")
    # source.drag_to(target)
    page.get_by_role("link", name="Sign In").click()
    page.locator("div")
    print(page)
    page.get_by_placeholder("username@example.com").click()
    page.get_by_placeholder("username@example.com").clear()
    page.get_by_placeholder("username@example.com").count()
    page.get_by_placeholder(
        "username@example.com").fill("vishnureddy12.in@gmail.com")
    page.get_by_placeholder("username@example.com").press("Enter")
    page.get_by_placeholder("username@example.com").clear()
    page.locator("#password").fill("vishnu")
    # page.locator("#password").press("CapsLock")
    page.locator("#password").fill("vishnu16REDDY@")
    page.locator("#password").press("Enter")
    page.locator(".wrapper-2-1-99").first.click()
    page.get_by_test_id("unifiedConsoleWidget_1").get_by_role(
        "link", name="EC2").click()
    page.get_by_role("link", name="Instances").first.click()
    page.frame_locator("#compute-react-frame").get_by_role("row",
                                                           name="– i-0fc7c4065a029ac00 Running t2.micro 2/2 checks passed No alarms ap-south-1a ec2-43-205-199-48.ap-south-1.compute.amazonaws.com 43.205.199.48 – – disabled launch-wizard-1 vishnu_reddy 2022/12/22 11:27 GMT+5:30").locator("label").click()
    page.frame_locator(
        "#compute-react-frame").get_by_role("button", name="Connect").click()
    with page.expect_popup() as page1_info:
        page.frame_locator(
            "#compute-react-frame").get_by_test_id("connect-button").click()
    page1 = page1_info.value
    page1.locator("//canvas[@class='xterm-cursor-layer']").click()
    time.sleep(3)
    page1.get_by_role("textbox", name="Terminal input").fill("clear")
    time.sleep(3)
    page1.get_by_role("textbox", name="Terminal input").press("Enter")
    time.sleep(3)
    page1.get_by_role("textbox", name="Terminal input").fill("ls")
    time.sleep(3)
    page1.get_by_role("textbox", name="Terminal input").press("Enter")
    time.sleep(3)
    page1.get_by_test_id("more-menu__awsc-nav-account-menu-button").click()
    page1.get_by_test_id("aws-console-signout").click()
