from helpers.download import downloadFiles
from time import sleep as esperar
from selenium.webdriver.common.by import By
from filtros.estado_equipos import poner_filtro_estado_equipo
from filtros.backlog_super import poner_filtro_backlog_super
from filtros.tipo_calendario import poner_filtro_tipo_calendario
from filtros.flota_y_work_group import poner_flota_and_work_group

def bajar_ots (driver, flota, grupo_de_trabajo):    
      
    poner_flota_and_work_group(driver, flota, grupo_de_trabajo)
    
    poner_filtro_estado_equipo(driver)
    poner_filtro_backlog_super(driver)
    poner_filtro_tipo_calendario(driver)
    
    esperar(1)
    if(flota == 'Camion240'):
        print('aqui')
        backlog_super = driver.find_element(By.XPATH, '//*[@id="37"]/div[3]/button')
        backlog_super.click()
        
    #Bajar las ots
    otsButton = driver.find_element(By.XPATH, '//*[@id="16"]/div[3]/div[1]/div[2]')
    esperar(1)
    otsButton.click()
    esperar(1)
    downloadFiles(driver, flota + "_ots.xls")