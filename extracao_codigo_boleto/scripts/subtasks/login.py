from playwright.sync_api import sync_playwright 
from time import sleep
from dotenv import load_dotenv
import os
load_dotenv()

def portal_aluno_login():
    url = os.getenv('SITE_URL')
    user = os.getenv('USER')
    passwd = os.getenv('PASSWD')
    with sync_playwright() as p:
        #Configuração inicial do playwright
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        #Abre o portal do aluno utilizando o chromium como navegador
        page.goto(url)
        sleep(2)

        #Clica no botão para inicar o login utilizando o e-mail acadêmico
        login_button = page.locator('//button[@id="login"]')
        login_button.click();
        sleep(2)
        
        
        #Preenche o campo e-mail 
        email_field = page.locator('//input[@type="email"]')
        email_field.fill(user)
        sleep(1)
        
        #Clica no botão para avançar
        avance_button = page.locator('//input[@type="submit"]')
        avance_button.click()
        sleep(1)

        #Preenche o campo senha
        passwd_field = page.locator('//input[@name="passwd"]')
        passwd_field.fill(passwd)

        #Clica no botão para logar
        sigin_button = page.locator('//input[@type="submit"]')
        sigin_button.click()
        sleep(1)
        
        #Clica no botão para não manter logado
        dnt_keep_login_button = page.locator('//input[@type="button"]')
        dnt_keep_login_button.click()
        context.storage_state(path="state.json")
        browser.close();