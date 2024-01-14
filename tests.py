import pytest
from app import app

#define a setup to test the app
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

#First Test: define a test for checking if the application is working, i.e,
#(home page returns a 200 status code and contains msg)
def test_app_is_working(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello World!" in response.data

#Second Test: check if a non-existent page returns a 404 status code
def test_non_existent_page(client):
    response = client.get('/nonexistent')
    assert response.status_code == 404

#Third Test: check if the app handles other routes properly
def test_other_routes(client):
    response = client.get('/other')
    assert response.status_code == 200
    assert b"This is another route" in response.data

