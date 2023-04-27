import os
import glob
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep as esperar
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import NoSuchElementException

download_dir = r"C:\lean\backlog_files" 
def downloadFiles (driver, newFileName):
    
    #Selecciono un elemento de la seccion pertinente (pestaña) de la cual bajar la informacion 
    if('ots' in newFileName):
        table = driver.find_element(By.XPATH, '//*[@id="43"]/div[2]/div[1]/div[1]/div[1]/div/div[4]')
    elif('agrietas' in newFileName):
        table = driver.find_element(By.XPATH, '//*[@id="43"]/div[2]/div[1]/div[1]/div[1]/div/div[3]/div[1]')
    else:
        table = driver.find_element(By.XPATH, '//*[@id="44"]/div[2]/div[1]/div[1]/div[1]/div/div[4]')
    
    #Click derecho sobre el elemento de la tabla de la pestaña                                    
    ActionChains(driver).context_click(table).perform()
    esperar(1)
    #En el menu emergente busco la opcion "Send to Excel" y doy click sobre ella
    excel = driver.find_element(By.XPATH, '/html/body/ul/li[11]/a')
    esperar(2)
    excel.click()
    
    #Espero a que se descargue el archivo para poder continuar
    esperar(6)
    
    #Obtengo la lista de archivos en la carpeta de destino
    files = glob.glob(os.path.join(download_dir, "*.xls"))
    
    #Ordeno los archivos por fecha de modificación, para elegir el ultimo que se añdio/modifico
    files.sort(key=os.path.getctime, reverse=True)
    filename = files[0]
    
    #Renombro el archivo
    os.replace(os.path.join(download_dir, filename), os.path.join(download_dir, newFileName))
    
    esperar(1)
    #Busco el modal que se genera cuando se descarga un archivo para darle click en "Ok"
    try:
        if('agrietas' in newFileName):
            okButton = driver.find_element(By.XPATH, '/html/body/div[18]/div[2]/button')
        else:
            okButton = driver.find_element(By.XPATH, '/html/body/div[16]/div[2]/button') 
        okButton.click()
    except (NoSuchElementException, ElementNotInteractableException) as e:
        print(e.msg)
        pass
    
    esperar(2)
