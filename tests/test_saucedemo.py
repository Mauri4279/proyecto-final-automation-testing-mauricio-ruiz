from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_exitoso(driver: WebDriver):
    """Verifica que un usuario pueda loguearse con credenciales válidas."""
    
    # 1. Navegar a la página
    driver.get("https://www.saucedemo.com/")
    
    # 2. Configurar la "Espera Explícita" (Máximo 10 segundos)
    wait = WebDriverWait(driver, 10)

    # 3. Interacción con los elementos web
    # Esperamos hasta que el campo de usuario aparezca en el HTML para escribir
    username_field = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
    username_field.send_keys("standard_user")
    
    # Como el campo anterior ya cargó, podemos asumir que la contraseña y el botón también están
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # 4. Validaciones (Asserts)
    # Validamos que la URL contenga "/inventory.html"
    wait.until(EC.url_contains("/inventory.html"))
    assert "/inventory.html" in driver.current_url, "Error: La URL no cambió a inventory.html"
    
    # Validamos que el título "Products" sea visible
    title_element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "title")))
    assert title_element.text == "Products", f"Error: Se esperaba 'Products', pero se encontró '{title_element.text}'"