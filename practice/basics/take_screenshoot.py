# To take screenshoot of the page

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.firefox.launch(headless = True, slow_mo= 40)
    page = browser.new_page()
    page.goto("https://playwright.dev")
    page.screenshot(path = "scrnshoot.jpeg")
    browser.close()
    
