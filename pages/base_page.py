from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    """Clase base que envuelve los métodos de Selenium con esperas explícitas."""
    
    def __init__(self, driver):
        self.driver = driver
        # Centralizamos la espera máxima en 10 segundos para todo el proyecto
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def find_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type_text(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text