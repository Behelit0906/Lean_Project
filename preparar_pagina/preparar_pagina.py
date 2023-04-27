from time import sleep as esperar
from selenium.webdriver.common.by import By
from excel.excel import fillBacklog
from preparar_pagina.detectar_alert import alert_is_present
from operaciones_archivos.bajar_ots import bajar_ots
from operaciones_archivos.bajar_mst import bajar_mst
from operaciones_archivos.bajar_agrietas import bajar_agrietas

def preparar_pagina(driver):
     # Navegar a una página web
    driver.get("http://lmnqvs01/QvAJAXZfc/opendoc.htm?document=mtto%5Cmto-trabajopendiente.qvw&host=QVS%40lmnqvs01")
    driver.maximize_window()
    driver.implicitly_wait(5)
    esperar(6)

    while True:
        i = alert_is_present(driver)
        if(i):
            driver.refresh()
            esperar(15)
        else:
            break

    esperar(5)  
    analisisPendienteButton = driver.find_element(By.XPATH, '//*[@id="Document\SH45"]/a')
    analisisPendienteButton.click()
    esperar(4) 
    
    flotas = {
            "Cam320": "EH320 - U.A.S. CAMIONES DE 320 MINA NORTE",
            "Kom320": "EH320 - U.A.S. CAMIONES DE 320 MINA NORTE",
            "Camion240": "CAT2401 - U.A.S. CAMIONES CAT240",
            "Car789C": 'CAT789C - Camion 190 ton "cat789C"',
            "Hit EX3600R": "PHIMARC-Hit EX3600R",
            "Hitachi EX5500": "PHIDCAS-Hitachi EX5500",
            "L1350": "CARGUE2 - U.A.S. DE CARGADORES FRONTALES",
            "LIE984C": "PHIDCAS-LIE984C",
            "MotoNiv 16M": "VIAS - UAS DE MOTONIVELADORAS Y TRAILLAS",
            "TraillaC631E": "VIAS - UAS DE MOTONIVELADORAS Y TRAILLAS",
            "P&H_XPC": "PHS-P&H_XPC",
            "TalDML35": "TALSEIS - GRUPO DE EJECUCION SEIS DE TALADROS",
            "TalDMLSP": "TALSEIS - GRUPO DE EJECUCION SEIS DE TALADROS",
            "TalPV271": "TALSEIS - GRUPO DE EJECUCION SEIS DE TALADROS",
            "Tanq. CAT": "TANQ777 - UAS DE TANQUEROS",
            "TOruga D9T": "ORUGAS - TRACTORES DE ORUGAS D9L Y D11N",
            "TOruga D10T": "ORUGAS - TRACTORES DE ORUGAS D9L Y D11N",
            "TOruga D11T": "ORUGAS - TRACTORES DE ORUGAS D9L Y D11N",
        }
    
    boton_limpiar = driver.find_element(By.XPATH, '//*[@id="QvAjaxToolbar-left"]/li[1]/a')
    boton_limpiar.click()
    esperar(4)

    for flota, grupo_de_trabajo in flotas.items():
        print(f"Flota: {flota}")
        while True:
            try:
                bajar_ots(driver, flota, grupo_de_trabajo)
                break
            except Exception as e:
                print("Error bajando las ots")
                print(str(e))
                
        
        while True:
            try:            
                # poner_filtros_basicos(driver)
                # esperar(1)
                # poner_flota_and_work_group(driver, flota, grupo_de_trabajo)
                # esperar(1)
                # bajar_ots(driver, flota, grupo_de_trabajo)
                bajar_mst(driver,flota, grupo_de_trabajo)
                # bajar_agrietas(driver, flota)
                break
            except Exception as e:
                print("Error bajando las mst")
                print(str(e))
                
        while True:
            try:
                bajar_agrietas(driver, flota, grupo_de_trabajo)
                break
            except Exception as e:
                print("Error bajando agrietas")
                print(str(e))
    
    driver.quit()
    fillBacklog()
                
