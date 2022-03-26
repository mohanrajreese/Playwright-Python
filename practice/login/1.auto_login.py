from playwright.sync_api import sync_playwright

with sync_playwright() as spw:
    browser = spw.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://github.com/login')

    # 
    page.locatclick('text=Login')
    page.fill('[name="login"]', 'mohanrajreese')
    page.fill('[name="password"]', '9843375583Moh@n')
    page.click('text=Submit')
