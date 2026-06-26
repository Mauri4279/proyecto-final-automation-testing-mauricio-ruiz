# tests/test_ui/test_saucedemo.py
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_login_exitoso(driver):
    """Verifica que un usuario pueda loguearse con credenciales válidas."""
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    assert "/inventory.html" in driver.current_url
    assert inventory_page.get_title() == "Products"

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