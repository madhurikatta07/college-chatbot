import pytest
import json
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health_endpoint(client):
    response = client.get('/health')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['status'] == 'healthy'

def test_chat_get_endpoint(client):
    response = client.get('/chat?msg=hello')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'response' in data
    assert 'confidence' in data
    assert data['predicted_intent'] in ['greeting', 'admission', 'courses', 'fees', 'goodbye']

def test_chat_post_endpoint(client):
    response = client.post('/chat', 
                          data=json.dumps({'msg': 'how do I apply'}),
                          content_type='application/json')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'response' in data
    assert 'predicted_intent' == 'admission'

def test_missing_message(client):
    response = client.get('/chat')
    assert response.status_code == 400
    data = json.loads(response.data)
    assert 'error' in data
