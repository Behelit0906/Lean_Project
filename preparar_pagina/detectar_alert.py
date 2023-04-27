def alert_is_present(driver):
    try:
        alert = driver.switch_to.alert
        alert.accept()
        return True
    except:
        return False
