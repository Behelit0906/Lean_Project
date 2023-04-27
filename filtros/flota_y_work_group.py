from time import sleep as esperar
from selenium.webdriver.common.by import By
from helpers.scroll import scroll_horizontal

def poner_flota_and_work_group(driver, flota, grupo_de_trabajo):
    ruta_sub_menu = '//*[@id="DS"]'
    seccion_ruta = '//*[@id="13"]'
    
    try:
        #Busco si la flota ya fue seleccionada
        seccion = driver.find_element(By.XPATH, seccion_ruta)
        filtro_flota = seccion.find_element(By.XPATH, f".//*[@title='{flota}']")
    except:
        # -------------- Seleccionando la flota ----------------------
        seccion_flotas = driver.find_element(By.XPATH, '//*[@id="10"]/div[3]/div/div[1]/div[5]/div/div[17]/div[2]/div/div')
        seccion_flotas.click()
        esperar(1)
        sub_menu = driver.find_element(By.XPATH, ruta_sub_menu)
        while True:
            try:
                opcion = sub_menu.find_element(By.XPATH, f".//*[@title='{flota}']")
                opcion.click()
                esperar(1)
                break
            except:
                scroll_horizontal(driver)
            
    try:
        #Busco si el grupo ya fue seleccionado
        seccion = driver.find_element(By.XPATH, seccion_ruta)
        filtro_grupo_de_trabajo = seccion.find_element(By.XPATH, f".//*[@title='{grupo_de_trabajo}']")
    except:  
    # ---------- Seleccionando el grupo de trabajo ----------------
        seccion_work_group = driver.find_element(By.XPATH, '//*[@id="10"]/div[3]/div/div[1]/div[5]/div/div[8]/div[2]/div/div')
        seccion_work_group.click()
        esperar(1)
        sub_menu = driver.find_element(By.XPATH, ruta_sub_menu)
        
        while True:
            try:
                opcion = sub_menu.find_element(By.XPATH, f".//*[@title='{grupo_de_trabajo}']")
                opcion.click()
                esperar(1)
                break
            except:
                scroll_horizontal(driver) 
                     
    
    