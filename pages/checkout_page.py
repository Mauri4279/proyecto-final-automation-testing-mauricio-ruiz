from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    # Localizadores
    CHECKOUT_BUTTON = (By.ID, "checkout")
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")

    # Acciones
    def start_checkout(self):
        self.click(self.CHECKOUT_BUTTON)

    def fill_personal_info(self, nombre, apellido, codigo_postal):
            # 1. Esperamos a que la página de Checkout realmente se haya cargado
            from selenium.webdriver.support import expected_conditions as EC
            self.wait.until(EC.url_contains("checkout-step-one.html"))
            
            # 2. Ahora sí, escribimos los datos
            self.type_text(self.FIRST_NAME, nombre)
            self.type_text(self.LAST_NAME, apellido)
            self.type_text(self.POSTAL_CODE, codigo_postal)
            self.click(self.CONTINUE_BUTTON)

    def finish_checkout(self):
        self.click(self.FINISH_BUTTON)

    def get_success_message(self):
        return self.get_text(self.COMPLETE_HEADER)