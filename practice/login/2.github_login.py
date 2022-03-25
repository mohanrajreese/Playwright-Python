from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://github.com/login
    page.goto("https://github.com/login")

    # Click input[name="login"]
    page.locator("input[name=\"login\"]").click()

    # Fill input[name="login"]
    page.locator("input[name=\"login\"]").fill("mohanrajreese")

    # Click input[name="password"]
    page.locator("input[name=\"password\"]").click()

    # Fill input[name="password"]
    page.locator("input[name=\"password\"]").fill("9843375583Moh@n")

    # Click input:has-text("Sign in")
    page.locator("input:has-text(\"Sign in\")").click()
    # expect(page).to_have_url("https://github.com/sessions/verified-device")

    # Click [placeholder="\36 -digit code"]
    page.locator("[placeholder=\"\\36 -digit code\"]").click()

    # Fill [placeholder="\36 -digit code"]
    # with page.expect_navigation(url="https://github.com/"):
    with page.expect_navigation():
        page.locator("[placeholder=\"\\36 -digit code\"]").fill("715754")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
