from playwright.sync_api import Playwright, sync_playwright, expect

def run(playwright: Playwright) -> None:

    # Arrange - Given
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    # Open new page
    page = context.new_page()
    # Go to https://symonstorozhenko.wixsite.com/website-1
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.set_default_timeout(5000)


    # Actions - When/And

    # Click button:has-text("Log In")
    # page.click("button:has-text(\"Log In\")", timeout=3000) # Wrong writing/Legacy
    # page.locator("button:has-text(\"Log In\")").click(timeout=2000)
    page.locator("text=Log in").click(timeout=2000)

    # Click [data-testid="signUp\.switchToSignUp"]
    page.locator("[data-testid=\"signUp\\.switchToSignUp\"]").click()
    # Click [data-testid="siteMembersDialogLayout"] [data-testid="buttonElement"]
    page.locator("[data-testid=\"siteMembersDialogLayout\"] [data-testid=\"buttonElement\"]").click()
    # Fill [data-testid="emailAuth"] input[type="email"]
    page.locator("[data-testid=\"emailAuth\"] input[type=\"email\"]").fill("muthematrix1@gmail.com")
    # Click input[type="password"]
    page.locator("input[type=\"password\"]").click()
    # Fill input[type="password"]
    page.locator("input[type=\"password\"]").fill("Pierre97")
    # Click [data-testid="submit"] [data-testid="buttonElement"]
    # page.locator("text=Log In").click(timeout=2000)
    page.locator("[data-testid=\"submit\"] [data-testid=\"buttonElement\"]").click()
    # Click [aria-label="muthematrix1 account menu"]
    page.locator("[aria-label=\"muthematrix1 account menu\"]").click()

    # Assert - Then
    assert page.locator("text=My Orders").is_visible()


    #
    # # Click text=My Orders
    # page.locator("text=My Orders").click()
    # page.wait_for_url("https://symonstorozhenko.wixsite.com/website-1/account/my-orders")
    # # Click [aria-label="muthematrix1 account menu"]
    # page.locator("[aria-label=\"muthematrix1 account menu\"]").click()
    # # Click [aria-label="muthematrix1 account menu"]
    # page.locator("[aria-label=\"muthematrix1 account menu\"]").click()
    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)