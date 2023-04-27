from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def scroll_horizontal(driver):
    acciones = ActionChains(driver)
    scroll_bar = driver.find_element(By.XPATH, '//*[@id="DS"]/div/div/div[2]')
    sleep(2)
    acciones.click_and_hold(scroll_bar)
    acciones.move_by_offset(0,35)
    acciones.release().perform()
    
