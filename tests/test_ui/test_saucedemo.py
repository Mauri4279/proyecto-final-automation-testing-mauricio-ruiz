import json
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage

# Función para cargar el archivo JSON
def cargar_datos_login():
    with open("data/credenciales.json", "r") as archivo:
        return json.load(archivo)

# def test_login_exitoso(driver):
#     """Verifica que un usuario pueda loguearse con credenciales válidas."""
#     login_page = LoginPage(driver)
#     inventory_page = InventoryPage(driver)

#     login_page.navigate()
#     login_page.login("standard_user", "secret_sauce")

#     assert "/inventory.html" in driver.current_url
#     assert inventory_page.get_title() == "Products"

@pytest.mark.parametrize("datos", cargar_datos_login())
def test_login_parametrizado(driver, datos):
    """Verifica el login con credenciales válidas e inválidas desde un JSON."""
    login_page = LoginPage(driver)
    
    login_page.navigate()
    login_page.login(datos["username"], datos["password"])

    if datos["resultado_esperado"] == "exito":
        assert "/inventory.html" in driver.current_url, "El login válido falló"
    else:
        mensaje_error = login_page.get_error_message()
        assert "locked out" in mensaje_error, "No se mostró el error de usuario bloqueado"

def test_verificar_catalogo(driver):
    """Verifica la presencia de productos en el catálogo."""
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    assert inventory_page.count_products() > 0, "No se encontraron productos."

def test_interaccion_con_carrito(driver):
    """Verifica que se pueda añadir un producto al carrito."""
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    inventory_page.add_first_product_to_cart()
    
    assert inventory_page.get_cart_badge_number() == "1", "El contador no muestra 1"

def test_flujo_checkout_completo(driver):
    """Verifica que un usuario pueda completar todo el proceso de compra."""
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    checkout_page = CheckoutPage(driver)

    # 1. Login
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    # 2. Añadir al carrito y navegar
    inventory_page.add_first_product_to_cart()
    inventory_page.go_to_cart()

    # 3. Proceso de Checkout
    checkout_page.start_checkout()
    checkout_page.fill_personal_info("Juan", "Perez", "1234")
    checkout_page.finish_checkout()

    # 4. Validación Final
    mensaje_final = checkout_page.get_success_message()
    assert mensaje_final == "Thank you for your order!", "El flujo de compra no finalizó correctamente"

def test_forzar_error_captura(driver):
    """Test diseñado específicamente para fallar y probar el sistema de capturas."""
    from pages.login_page import LoginPage
    
    # 1. Navegamos a la página
    login_page = LoginPage(driver)
    login_page.navigate()
    
    # 2. Forzamos el fallo: Afirmamos que el título es "Facebook" (cuando en realidad es "Swag Labs")
    assert driver.title == "Facebook", "🚨 Este error es 100% intencional para generar el screenshot 🚨"