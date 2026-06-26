import logging
import os

def get_logger(name="AutomationFramework"):
    """Configura y devuelve un logger personalizado."""
    logger = logging.getLogger(name)
    
    # Evitar que se dupliquen los logs si se llama varias veces
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        
        # Asegurarnos de que la carpeta reports exista
        os.makedirs("reports", exist_ok=True)
        
        # Formato del log: Fecha/Hora - Nivel - Mensaje
        formato = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        
        # Handler 1: Guardar en un archivo (automation.log)
        file_handler = logging.FileHandler("reports/automation.log", encoding="utf-8")
        file_handler.setFormatter(formato)
        logger.addHandler(file_handler)
        
        # Handler 2: Imprimir en la consola de la terminal
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formato)
        logger.addHandler(console_handler)
        
    return logger