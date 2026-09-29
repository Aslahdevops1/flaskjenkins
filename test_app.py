from app import app


def test_home():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert b"Hello, GitHub Actions!" in response.data


def test_about():
    client = app.test_client()
    response = client.get("/about")

    assert response.status_code == 200
    assert b"About Page" in response.data