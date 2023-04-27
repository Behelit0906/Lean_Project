from helpers.download import downloadFiles
from time import sleep as esperar
from selenium.webdriver.common.by import By
from filtros.estado_equipos import poner_filtro_estado_equipo
from filtros.backlog_super import poner_filtro_backlog_super
from filtros.tipo_calendario import poner_filtro_tipo_calendario
from filtros.flota_y_work_group import poner_flota_and_work_group

def bajar_mst(driver, flota, grupo_de_trabajo):
    if (flota != 'Hit EX3600R' and flota != 'Hitachi EX5500'):
        poner_flota_and_work_group(driver, flota, grupo_de_trabajo)
        
        poner_filtro_estado_equipo(driver)
        poner_filtro_backlog_super(driver)
        poner_filtro_tipo_calendario(driver)
                
        #Bajar las mst
        mstButton = driver.find_element(By.XPATH, '//*[@id="16"]/div[3]/div[1]/div[3]')
        esperar(1)
        mstButton.click()
        esperar(1)
        downloadFiles(driver, flota + "_mst.xls")