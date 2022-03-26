from playwright.sync_api import Playwright, sync_playwright, expect

mobile_numbers = ["9993070611","9617449210","9250875036"]
with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    page = context.new_page()

    page.goto("https://channel.lendingkart.com/dsachannelpartner-xlr8/partner/login")

    page.locator("text=click here").click()

    page.locator("[placeholder=\"Enter Email ID\"]").click()

    page.locator("[placeholder=\"Enter Email ID\"]").fill("sreedhar@propwiser.com")

    page.locator("[placeholder=\"Password\"]").click()

    page.locator("[placeholder=\"Password\"]").fill("Loanwiser@123")

    with page.expect_navigation():
        page.locator("button:has-text(\"Login\")").click()

    page.locator("[placeholder=\"Search by Lead ID\\, Application ID\\, Company Name\\, Email or Contact Number\"]").click()

    page.locator("[placeholder=\"Search by Lead ID\\, Application ID\\, Company Name\\, Email or Contact Number\"]").fill(mobile_numbers[1])

    page.locator("[placeholder=\"Search by Lead ID\\, Application ID\\, Company Name\\, Email or Contact Number\"]").press("Enter")

    page.pause()

    context.close()
    browser.close()
