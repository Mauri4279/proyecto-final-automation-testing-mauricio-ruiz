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

def test_verificar_catalogo(driver):
    """Verifica el título de la página, presencia de productos y elementos de UI."""
    
    # 1. Login rápido (Precondición para acceder al catálogo)
    driver.get("https://www.saucedemo.com/")
    wait = WebDriverWait(driver, 10)
    
    wait.until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # 2. Verificar que el título de la página sea correcto
    title_element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "title")))
    assert title_element.text == "Products", "Error: El título no es 'Products'"

    # 3. Comprobar que existan productos visibles (al menos uno)
    # Usamos presence_of_all_elements_located para obtener una lista (array) de elementos
    productos = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item")))
    assert len(productos) > 0, "Error: No se encontraron productos en el catálogo"

    # 4. Listar nombre y precio del primer producto
    primer_nombre = productos[0].find_element(By.CLASS_NAME, "inventory_item_name").text
    primer_precio = productos[0].find_element(By.CLASS_NAME, "inventory_item_price").text
    print(f"\n--- Info del primer producto: {primer_nombre} | Precio: {primer_precio} ---")

    # 5. Validar que elementos importantes de la interfaz estén presentes
    menu_btn = driver.find_element(By.ID, "react-burger-menu-btn")
    assert menu_btn.is_displayed(), "Error: El botón de menú no es visible"
    
    filtro_dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container")
    assert filtro_dropdown.is_displayed(), "Error: El filtro de productos no es visible"

def test_interaccion_con_carrito(driver):
    """Verifica que se pueda añadir un producto al carrito y aparezca allí."""
    
    # 1. Login rápido (Precondición)
    driver.get("https://www.saucedemo.com/")
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # 2. Añadir el primer producto al carrito
    # Buscamos todos los botones que tengan el texto "Add to cart" usando XPATH
    botones_add = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//button[text()='Add to cart']")))
    botones_add[0].click()

    # 3. Verificar que el contador del carrito se incremente correctamente
    badge_carrito = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
    assert badge_carrito.text == "1", "Error: El contador del carrito no muestra 1"

    # 4. Navegar al carrito de compras
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # 5. Comprobar que el producto añadido aparezca correctamente en el carrito
    wait.until(EC.url_contains("/cart.html"))
    items_en_carrito = driver.find_elements(By.CLASS_NAME, "cart_item")
    
    # Validamos que haya exactamente 1 elemento en la lista del carrito
    assert len(items_en_carrito) == 1, "Error: El producto no aparece en el carrito"