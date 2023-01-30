from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    # Open new page
    page = context.new_page()
    # Go to https://chatbocarvajaltest.000webhostapp.com/
    page.goto("https://chatbocarvajaltest.000webhostapp.com/")
    # Click text=Gracias por contactarte con Carvajal Tecnología y Servicios. Indícanos a continu
    page.locator("text=Gracias por contactarte con Carvajal Tecnología y Servicios. Indícanos a continu").click()
    # Click text=Soporte
    page.locator("text=Soporte").click()
    # Click text=Factura Electronica
    page.locator("text=Factura Electronica").click()
    # Click text=Atras
    page.locator("text=Atras").click()
    # Click text=Queja, peticion o reclamo >> nth=1
    page.locator("text=Queja, peticion o reclamo").nth(1).click()
    # Click text=Atras >> nth=2
    page.locator("text=Atras").nth(2).click()
    # Click text=Interes sobre un producto >> nth=2
    page.locator("text=Interes sobre un producto").nth(2).click()
    # Click text=Factura Electronica >> nth=2
    page.locator("text=Factura Electronica").nth(2).click()
    # Click text=Atras >> nth=4
    page.locator("text=Atras").nth(4).click()
    # Click text=Interes sobre un producto >> nth=4
    page.locator("text=Interes sobre un producto").nth(4).click()
    # Click text=CEN >> nth=2
    page.locator("text=CEN").nth(2).click()
    # Click a:has-text("Atras") >> nth=3
    page.locator("a:has-text(\"Atras\")").nth(3).click()
    # Click a:has-text("Interes sobre un producto") >> nth=4
    page.locator("a:has-text(\"Interes sobre un producto\")").nth(4).click()
    # Click text=CONRED >> nth=3
    page.locator("text=CONRED").nth(3).click()
    # Click a:has-text("Atras") >> nth=4
    page.locator("a:has-text(\"Atras\")").nth(4).click()
    # ---------------------
    # context.close()
    # browser.close()


with sync_playwright() as playwright:
    run(playwright)
