from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_moods():
    response = client.get("/moods")
    assert response.status_code == 200
    data = response.json()
    assert "moods" in data
    assert isinstance(data["moods"], list)


def test_get_music_valid():
    response = client.get("/music?mood=happy")
    assert response.status_code == 200
    assert "songs" in response.json()

def test_get_music_invalid():
    response = client.get("/music?mood=angry")
    assert response.status_code == 404
