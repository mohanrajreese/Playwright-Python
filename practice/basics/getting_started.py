# Synchronous method

from playwright.sync_api import sync_playwright

with sync_playwright() as pw:
    browser = pw.firefox.launch()
    page = browser.new_page()
    page.goto("https://github.com/")
    print(page.title())
    browser.close()

    
# # asyncio method
import asyncio
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as apw:
        browser = await apw.firefox.launch(headless= True)
        page = await browser.new_page()
        await page.goto("https://github.com/")
        print (await page.title())
        await browser.close()

asyncio.run(main())
