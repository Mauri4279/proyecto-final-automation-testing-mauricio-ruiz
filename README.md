# Proyecto de Automatización QA - Pre-Entrega

## Propósito del Proyecto
Este proyecto es el Trabajo Final Integrador para el curso de QA Automation de Talento Tech impartida por la Agencia de Habilidades para el Futuro. El objetivo es desarrollar un framework de automatización de pruebas completo que combina pruebas de interfaz de usuario (UI) y pruebas de API. El sitio objetivo de las pruebas es la plataforma de e-commerce de prueba [Saucedemo](https://www.saucedemo.com/).

El framework está estructurado utilizando el patrón **Page Object Model (POM)** para las pruebas de UI, garantizando eficiencia y mantenibilidad, y utiliza la biblioteca Requests para las validaciones de API. Se implementan buenas prácticas, generación de reportes detallados y manejo de datos externos.

## Tecnologías Utilizadas
* **Lenguaje:** Python 3
* **Automatización UI:** Selenium WebDriver
* **Pruebas de API:** Requests
* **Framework de Testing:** Pytest
* **Reportes:** Pytest-HTML
* **Gestión de Drivers:** Webdriver-Manager
* **Control de Versiones:** Git y GitHub

## Estructura del Proyecto
El proyecto sigue una organización modular basada en POM:
* `pages/`: Contiene las clases que representan las páginas web y sus acciones.
* `tests/`: Separación lógica entre pruebas de UI (`test_ui/`) y pruebas de API (`test_api/`).
* `utils/`: Funciones auxiliares y configuraciones (ej. WebDriver factory).
* `data/`: Archivos externos para parametrización de pruebas (CSV, JSON).
* `reports/`: Destino de los reportes HTML generados y capturas de pantalla de fallos.

## Instrucciones de Instalación

1. Clonar este repositorio:
   ```bash
   git clone https://github.com/Mauri4279/proyecto-final-automation-testing-mauricio-ruiz.git
   ```

2. Crear un entorno virtual:
   ```bash
   python -m venv venv
   ```

3. Activar el entorno virtual:  
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`

4. Instalar las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Ejecución de Pruebas y Reportes

Para ejecutar todas las pruebas (UI y API) y generar el reporte HTML con logs y capturas, utiliza el siguiente comando:

```bash
python -m pytest tests/test_saucedemo.py -v --html=reports/reporte.html
python -m pytest tests/test_api/test_reqres_api.py -v -s
```


### ¿Cómo interpretar los reportes generados?
El reporte HTML generado en `reports/reporte.html` proporciona una visión detallada de la ejecución. Mostrará cada test ejecutado, su duración y su estado:
* **Passed (Verde):** La prueba se ejecutó correctamente.
* **Failed (Rojo):** La prueba falló. En caso de pruebas de UI fallidas, el reporte o la carpeta `reports/screenshots/` incluirá una captura de pantalla automática con la fecha y hora del error para facilitar la depuración, además de los logs de ejecución.