from playwright.sync_api import Playwright, sync_playwright, expect

mobile_numbers = ["9993070611","9617449210","9250875036"]
with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False,slow_mo=30)
    context = browser.new_context()

    page = context.new_page()

    page.goto("https://channel.lendingkart.com/dsachannelpartner-xlr8/partner/login")

    page.locator("text=click here").click()

    username = page.locator("[placeholder=\"Enter Email ID\"]")
    username.click()
    username.fill("sreedhar@propwiser.com")

    password = page.locator("[placeholder=\"Password\"]")
    password.click()
    password.fill("Loanwiser@123")

    with page.expect_navigation():
        page.locator("button:has-text(\"Login\")").click()

    
    for number in range (len(mobile_numbers)):
        
        search_box = page.locator("[placeholder=\"Search by Lead ID\\, Application ID\\, Company Name\\, Email or Contact Number\"]")
        
        search_box.click()

        search_box.fill(mobile_numbers[number])

        search_box.press("Enter")

        Status = page.locator('//*[@id="scroll-container"]/app-home/div/div[3]/app-grid-list/div/div[2]/mat-table/mat-row[1]/mat-cell[4]/p[1]')
        Sub_Status = page.locator('//*[@id="scroll-container"]/app-home/div/div[3]/app-grid-list/div/div[2]/mat-table/mat-row[1]/mat-cell[4]/p[2]')
        print(mobile_numbers[number], Status.all_inner_texts(), Sub_Status.all_inner_texts())
        
        page.locator("[placeholder=\"Search by Lead ID\\, Application ID\\, Company Name\\, Email or Contact Number\"]").click()
        # page.video
    # page.pause()

    context.close()
    browser.close()
