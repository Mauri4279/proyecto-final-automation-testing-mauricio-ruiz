# Proyecto de Automatización QA - Pre-Entrega

## Propósito del Proyecto
Este proyecto es una pre-entrega para el curso de QA Automation de Talento Tech impartida por la Agencia de Habilidades para el Futuro; que demuestra la capacidad para automatizar flujos básicos de navegación web utilizando el patrón de Page Object Model (POM) o scripts modulares. El sitio objetivo de las pruebas es la plataforma de e-commerce de prueba [Saucedemo](https://www.saucedemo.com/).

## Tecnologías Utilizadas
* **Lenguaje:** Python 3
* **Automatización:** Selenium WebDriver
* **Framework de Testing:** Pytest
* **Reportes:** Pytest-HTML
* **Gestión de Drivers:** Webdriver-Manager

## Instrucciones de Instalación

1. Clonar este repositorio:
   ```bash
   git clone [URL_DE_TU_REPOSITORIO]
   ```

2. Crear un entorno virtual:
    ```bash
    python -m venv venv
    ```

3. Activar el entorno virtual:  
    - Windows: venv\Scripts\activate

    - Mac/Linux: source venv/bin/activate

4. Instalar las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

## Comando para Ejecutar las Pruebas y Generar Reporte
Para correr todos los casos de prueba y generar el reporte HTML automáticamente, ejecutar el siguiente comando en la terminal:
    ```bash
    python -m pytest tests/test_saucedemo.py -v --html=reports/reporte.html
    ```
El reporte se guardará en la carpeta reports/ bajo el nombre reporte.html.