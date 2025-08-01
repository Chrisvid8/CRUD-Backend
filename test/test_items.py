import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from app import create_app, db
from app.modules.item.model import Item

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

def test_create_item(client):
    response = client.post('/api/items/', json={
        'name': 'Test User',
        'phone': '1234567890',
        'email': 'test@example.com'
    })
    assert response.status_code == 201
    assert response.json['name'] == 'Test User'

def test_get_items(client):
    client.post('/api/items/', json={
        'name': 'User 1', 'phone': '123', 'email': 'user1@example.com'
    })
    response = client.get('/api/items/')
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_update_item(client):
    create = client.post('/api/items/', json={
        'name': 'Old Name', 'phone': '111', 'email': 'old@example.com'
    })
    item_id = create.json['id']
    response = client.put(f'/api/items/{item_id}', json={
        'name': 'New Name'
    })
    assert response.status_code == 200
    assert response.json['name'] == 'New Name'

def test_delete_item(client):
    create = client.post('/api/items/', json={
        'name': 'Delete Me', 'phone': '000', 'email': 'del@example.com'
    })
    item_id = create.json['id']
    response = client.delete(f'/api/items/{item_id}')
    assert response.status_code == 200
    assert response.json['message'] == 'Item deleted successfully'