import pytest
import os
from datetime import datetime
from utils.driver_factory import get_driver
from utils.logger import get_logger

log = get_logger()

@pytest.fixture
def driver():
    """Fixture que provee una instancia de WebDriver."""
    driver = get_driver()
    yield driver
    driver.quit()

# Gancho (Hook) para capturas automáticas en fallos
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # Si el test falló durante la ejecución ("call")
    if report.when == "call" and report.failed:
        # Obtenemos el driver del test fallido
        if "driver" in item.fixturenames:
            web_driver = item.funcargs["driver"]
            
            # Crear ruta reports/screenshots/
            screenshot_dir = os.path.join("reports", "screenshots")
            os.makedirs(screenshot_dir, exist_ok=True)
            
            # Formatear el nombre: nombre_del_test + fecha_hora.png
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            test_name = item.name # Extrae el nombre de la función de prueba
            screenshot_name = f"{test_name}_{timestamp}.png"
            screenshot_path = os.path.join(screenshot_dir, screenshot_name)
            
            # Guardar la imagen
            web_driver.save_screenshot(screenshot_path)
            log.error(f"❌ TEST FALLIDO: {test_name}. Captura guardada en: {screenshot_path}")