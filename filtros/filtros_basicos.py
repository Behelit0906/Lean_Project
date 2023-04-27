from time import sleep as esperar
from selenium.webdriver.common.by import By
from filtros.estado_equipos import poner_filtro_estado_equipo

def poner_filtros_basicos(driver):
    ruta_sub_menu = '//*[@id="DS"]'
    boton_limpiar = driver.find_element(By.XPATH, '//*[@id="QvAjaxToolbar-left"]/li[1]/a')
    boton_limpiar.click()
    esperar(4)
    
    # ------------ Poniendo el primer filtro -----------------------
    poner_filtro_estado_equipo(driver)
    # filtro_estado_equipos = driver.find_element(By.XPATH, '//*[@id="10"]/div[3]/div/div[1]/div[5]/div/div[27]')
    # filtro_estado_equipos.click()
    # esperar(1)
    # sub_menu = driver.find_element(By.XPATH, ruta_sub_menu)
    # opcion = sub_menu.find_element(By.XPATH, ".//*[@title='En operación']")
    # opcion.click()
    # esperar(1)
    
    
    # ------------ Poniendo el segundo filtro -----------------------
    backlog_super = driver.find_element(By.XPATH, '//*[@id="37"]/div[3]/button')
    esperar(1)
    backlog_super.click()
    esperar(2)
    while True:
        try:
            trabajo_pendiente_actual = driver.find_element(By.XPATH, '//*[@id="13"]/div[3]/div/div[1]/div[5]/div/div[4]/div[1]')
            break
        except:
            backlog_super.click()
            esperar(1)
    
    
    # ------------ Poniendo el tercer filtro ------------------------      
    tipo_calendario = driver.find_element(By.XPATH, '//*[@id="10"]/div[3]/div/div[1]/div[5]/div/div[33]')
    tipo_calendario.click()
    esperar(1)
    sub_menu = driver.find_element(By.XPATH, ruta_sub_menu)
    opcion = sub_menu.find_element(By.XPATH, ".//*[@title='Según Fecha Máxima de Atención']")
    opcion.click()
    esperar(2)
    
    esperar(2)
    