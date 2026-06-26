import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_post():
    """Valida la obtención de un post (GET)."""
    response = requests.get(f"{BASE_URL}/posts/1", verify=False)
    assert response.status_code == 200, f"Error HTTP {response.status_code}"
    
    json_data = response.json()
    assert "title" in json_data, "El JSON no tiene título"
    assert json_data["id"] == 1, "El ID no es el esperado"

def test_create_post():
    """Valida la creación de un post (POST)."""
    payload = {"title": "Test Title", "body": "Test Body", "userId": 1}
    response = requests.post(f"{BASE_URL}/posts", json=payload, verify=False)
    assert response.status_code == 201, f"Error HTTP {response.status_code}"
    
    json_data = response.json()
    assert json_data["title"] == payload["title"], "El título guardado no coincide"
    assert "id" in json_data, "No se generó ID"

def test_delete_post():
    """Valida la eliminación (DELETE)."""
    response = requests.delete(f"{BASE_URL}/posts/1", verify=False)
    # JSONPlaceholder devuelve 200 al borrar, en lugar del 204 estándar
    assert response.status_code == 200, f"Error HTTP {response.status_code}"

def test_api_lifecycle():
    """Prueba E2E de creación, modificación y borrado."""
    print("\n--- Iniciando E2E API ---")
    
    payload = {"title": "Creado", "body": "123", "userId": 1}
    res_post = requests.post(f"{BASE_URL}/posts", json=payload, verify=False)
    assert res_post.status_code == 201
    post_id = res_post.json()["id"]
    
    # JSONPlaceholder no permite modificar posts que creaste "falsamente", 
    # así que modificamos uno existente (ID 1)
    payload_mod = {"id": 1, "title": "Modificado", "body": "123", "userId": 1}
    res_put = requests.put(f"{BASE_URL}/posts/1", json=payload_mod, verify=False)
    assert res_put.status_code == 200
    assert res_put.json()["title"] == "Modificado"

    res_del = requests.delete(f"{BASE_URL}/posts/1", verify=False)
    assert res_del.status_code == 200