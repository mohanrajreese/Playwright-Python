from playwright.sync_api import sync_playwright

with sync_playwright() as spw:
    browser = spw.chromium.launch(headless = False)
    context = browser.new_context()
    page = context.new_page()
    
    page.goto("https://github.com/login")
    login = page.locator("[id=\"login_field\"]")
    login.click()
    login.fill("mohanrajreese")
    password = page.locator("[name=\"password\"]")
    password.click()
    password.fill("9843375583Moh@n")
    login = page.locator("[value=\"Sign in\"]")
    login.click()
    dropdown = page.locator("[aria-label=\"View profile and more\"]")
    dropdown.click()
    repo = page.locator("[data-ga-click=\"Header, go to repositories, text:your repositories\"]")
    repo.click()
    sel_repo = page.locator("[href=\"/mohanrajreese/Playwright-Python\"]")
    sel_repo.click()
    ins_repo = page.locator("feature-callout summary span")   
    ins_repo.click()
    page.pause()
    