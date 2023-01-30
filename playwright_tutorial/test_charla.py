from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to http://demo.testim.io/
    page.goto("http://demo.testim.io/")

    # Click text=Log in
    page.locator("text=Log in").click()
    page.wait_for_url("http://demo.testim.io/login")

    # Click text=UsernamePassword >> input[type="text"]
    page.locator("text=UsernamePassword >> input[type=\"text\"]").click()

    # Fill text=UsernamePassword >> input[type="text"]
    page.locator("text=UsernamePassword >> input[type=\"text\"]").fill("Tester")

    # Press Tab
    page.locator("text=UsernamePassword >> input[type=\"text\"]").press("Tab")

    # Fill input[type="password"]
    page.locator("input[type=\"password\"]").fill("12345")

    # Click nav >> text=Log in
    page.locator("nav >> text=Log in").click()
    page.wait_for_url("http://demo.testim.io/")

    # Localizar  - Ejecutar - Validar (Given-When-Then)

    assert page.locator("text=Hello,").is_visible()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
