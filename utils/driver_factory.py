from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def get_driver():
    """Inicializa y devuelve una instancia de Chrome WebDriver."""
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
    driver.maximize_window()
    return driver