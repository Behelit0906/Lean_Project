from helpers.download import downloadFiles
from time import sleep as esperar
from selenium.webdriver.common.by import By
from filtros.estado_equipos import poner_filtro_estado_equipo
from filtros.backlog_super import poner_filtro_backlog_super
from filtros.tipo_calendario import poner_filtro_tipo_calendario
from filtros.flota_y_work_group import poner_flota_and_work_group

def bajar_agrietas(driver, flota, grupo_de_trabajo):
    if(flota != 'LIE984C' and flota != 'Hitachi EX5500' and flota != 'Hit EX3600R'):
        
        poner_flota_and_work_group(driver, flota, grupo_de_trabajo)
      
        poner_filtro_estado_equipo(driver)
        poner_filtro_backlog_super(driver)
        poner_filtro_tipo_calendario(driver)
        otsButton = driver.find_element(By.XPATH, '//*[@id="16"]/div[3]/div[1]/div[2]')
        esperar(1)
        otsButton.click()
        esperar(1)
        
        # -------------------------------------
        seccion_work_group = driver.find_element(By.XPATH, '//*[@id="10"]/div[3]/div/div[1]/div[5]/div/div[8]/div[2]/div/div')
        seccion_work_group.click()
        esperar(1)
        sub_menu = driver.find_element(By.XPATH, ruta_sub_menu)
        ruta_sub_menu = '//*[@id="DS"]'
        columna_de_tabla = driver.find_element(By.XPATH, '//*[@id="43"]/div[2]/div[1]/div[1]/div[1]/div/div[2]')
        columna_de_tabla.click()
        sub_menu = driver.find_element(By.XPATH, ruta_sub_menu)
        opcion = sub_menu.find_element(By.XPATH, ".//*[@title='AGRIETA - Analisis de Grietas Equipos Mineros']")
        opcion.click()
        
        esperar(1)
        downloadFiles(driver, flota + '_agrietas.xls')