from app.api import app

def test_seccess():
    client = app.test_client()
    response = client.post('/reservations', json={
        "room": "A",
        "time": "14:00"
    })
    assert response.status_code == 201

def test_failure():
    client = app.test_client()
    client.post('/reservations', json={
        "room": "A",
        "time": "14:00"
    })
    response = client.post('/reservations', json={
        "room": "A",
        "time": "14:00"
    })
    assert response.status_code == 409
    assert response.get_json() == {"message": "Reservation cannot be made due to conflict"}