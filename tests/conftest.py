import pytest
from utils.driver_factory import get_driver

@pytest.fixture
def driver():
    """Fixture que provee una instancia de WebDriver."""
    driver = get_driver()
    yield driver # Aquí se ejecutan los tests
    driver.quit() # Esto se ejecuta al terminar el test