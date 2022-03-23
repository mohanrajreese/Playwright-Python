from playwright.sync_api import sync_playwright

with sync_playwright() as spw:
    browser = spw.chromium.launch(headless=False, slow_mo=100, devtools=True)
    context = browser.new_context()

    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page = context.new_page()
    page.goto("https://loanwiser.in")

    context.tracing.stop(path="F:\\playwright_python\\results\\trace.zip")
