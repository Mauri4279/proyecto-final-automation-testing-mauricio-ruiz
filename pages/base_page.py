from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import get_logger 

# Inicializamos el logger
log = get_logger()

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def find_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click(self, locator):
        log.info(f"Haciendo clic en el elemento: {locator}")  # <--- Agregamos Log
        try:
            self.wait.until(EC.element_to_be_clickable(locator)).click()
        except Exception as e:
            log.error(f"Fallo al hacer clic en {locator}. Detalle: {e}") # <--- Log de Error
            raise

    def type_text(self, locator, text):
        # Evitamos loguear contraseñas
        texto_seguro = "********" if "password" in str(locator).lower() else text
        log.info(f"Escribiendo '{texto_seguro}' en el elemento: {locator}") # <--- Agregamos Log
        
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            element.clear()
            element.send_keys(text)
        except Exception as e:
            log.error(f"Fallo al escribir en {locator}. Detalle: {e}")
            raise

    def get_text(self, locator):
        log.info(f"Obteniendo texto del elemento: {locator}") # <--- Agregamos Log
        return self.wait.until(EC.visibility_of_element_located(locator)).text