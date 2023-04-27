from time import sleep as esperar
from selenium.webdriver.common.by import By

def poner_filtro_backlog_super(driver):
    seccion_ruta = '//*[@id="13"]'
    backlog_super = driver.find_element(By.XPATH, '//*[@id="37"]/div[3]/button')
    backlog_super.click()
    esperar(1)
    while True:
        try:
            seccion = driver.find_element(By.XPATH, seccion_ruta)
            filtro_backlog_super = seccion.find_element(By.XPATH, ".//*[@title='FLAG_TIEMPO_TRABAJO']")
            break;
        except:
            backlog_super.click()
            esperar(1)