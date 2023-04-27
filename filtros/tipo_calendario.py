from time import sleep as esperar
from selenium.webdriver.common.by import By

def poner_filtro_tipo_calendario(driver):
    ruta_sub_menu = '//*[@id="DS"]'
    seccion_ruta = '//*[@id="13"]'
    try:
        seccion = driver.find_element(By.XPATH, seccion_ruta)
        filtro_tipo_calendario = seccion.find_element(By.XPATH, ".//*[@title='Según Fecha Máxima de Atención']")
    except:
        filtro_tipo_calendario = driver.find_element(By.XPATH, '//*[@id="10"]/div[3]/div/div[1]/div[5]/div/div[33]')
        filtro_tipo_calendario.click()
        esperar(1)
        sub_menu = driver.find_element(By.XPATH, ruta_sub_menu)
        opcion = sub_menu.find_element(By.XPATH, ".//*[@title='Según Fecha Máxima de Atención']")
        opcion.click()
        esperar(1)