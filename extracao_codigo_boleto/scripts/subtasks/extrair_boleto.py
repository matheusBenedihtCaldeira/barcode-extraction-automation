from playwright.sync_api import sync_playwright
from time import sleep

def portal_aluno_extrair_boleto():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False);
        context = browser.new_context(storage_state="state.json");
        page = context.new_page();
        page.goto('https://novoportal.cruzeirodosul.edu.br/gfa/home')
        sleep(2);
        finance_button = page.locator('//li[@title="Financeiro"]');
        finance_button.click();
        sleep(2);
        popup_button = page.locator('//button[@id="fecharmodal"]');
        if popup_button != None:
            popup_button.click();
        payment_option = page.locator('//span[@id="Fazer Pagamentos / Acordos"]');
        payment_option.click();
        sleep(2);
        mounth_ticket = page.locator('div.check').nth(0);
        mounth_ticket.click();
        sleep(2);
        generate_ticket_button = page.locator('//button[@id="btn-pgto-boleto"]');
        with context.expect_page() as new_page_info:
            generate_ticket_button.click();
        new_page = new_page_info.value
        new_page.wait_for_load_state()
        sleep(50)
        print(pyautogui.position())
        browser.close();
