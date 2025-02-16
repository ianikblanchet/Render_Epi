import pytest
from fastapi.testclient import TestClient
from main import app
import schemas
import requests

# client = TestClient(app)

# def test_read_epis():
#     response = client.get("/epis/")
#     assert response.status_code == 200
#     assert response.json() #== [{'id': 1, 'name': 'Casque'}, {'id': 2, 'name': 'Lunettes'}, {'id': 3, 'name': 'Gants'}, {'id': 4, 'name': 'Chaussures'}, {'id': 5, 'name': 'Veste'}]



BASE_URL = "http://127.0.0.1:8000"

def test_read_main():
    response = requests.get(f"{BASE_URL}/fab/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

    

if __name__ == "__main__":
    test_read_main()
    #test_create_item()
    print("All tests passed!")