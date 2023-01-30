from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    # Assess - Given
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    # Open new page
    page = context.new_page()
    # Go to https://richybernal13.wixsite.com/trackerx
    page.goto("https://richybernal13.wixsite.com/trackerx")
    page.set_default_timeout(7000)

    # Actions - When/And
    # Click button:has-text("Iniciar sesión")
    page.locator("button:has-text(\"Iniciar sesión\")").click(timeout=3000)
    # Click [data-testid="signUp\.switchToSignUp"]
    page.locator("[data-testid=\"signUp\\.switchToSignUp\"]").click()
    # Click [data-testid="siteMembersDialogLayout"] [data-testid="buttonElement"]
    page.locator("[data-testid=\"siteMembersDialogLayout\"] [data-testid=\"buttonElement\"]").click()
    # Fill [data-testid="emailAuth"] input[type="email"]
    page.locator("[data-testid=\"emailAuth\"] input[type=\"email\"]").fill("muthematrix1@gmail.com")
    # Click input[type="password"]
    page.locator("input[type=\"password\"]").click()
    # Fill input[type="password"]
    page.locator("input[type=\"password\"]").fill("T7n53z2q")
    # Click [data-testid="submit"] [data-testid="buttonElement"]
    page.locator("[data-testid=\"submit\"] [data-testid=\"buttonElement\"]").click()
    # Click [aria-label="muthematrix1 account menu"]
    page.locator("[aria-label=\"muthematrix1 account menu\"]").click()

    # Assert - Then
    assert page.locator("text=Mi cuenta").is_visible()

    # # Click text=Mi cuenta
    # page.locator("text=Mi cuenta").click()
    # page.wait_for_url("https://richybernal13.wixsite.com/trackerx/account/my-account")
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
