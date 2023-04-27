from time import sleep as esperar
from selenium.webdriver.common.by import By

def poner_filtro_estado_equipo(driver):
    ruta_sub_menu = '//*[@id="DS"]'
    seccion_ruta = '//*[@id="13"]'
    try:
        seccion = driver.find_element(By.XPATH, seccion_ruta)
        filtro_tipo_calendario = seccion.find_element(By.XPATH, ".//*[@title='FLAG_FUERA_OPER']")
    except:
        print("No encontré el estado de equipo")
        filtro_estado_equipos = driver.find_element(By.XPATH, '//*[@id="10"]/div[3]/div/div[1]/div[5]/div/div[27]')
        filtro_estado_equipos.click()
        esperar(1)
        sub_menu = driver.find_element(By.XPATH, ruta_sub_menu)
        opcion = sub_menu.find_element(By.XPATH, ".//*[@title='En operación']")
        opcion.click()
        esperar(1)

    
