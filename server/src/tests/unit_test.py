from src import Constants
from flask import Flask
import json
import pytest

@pytest.fixture
def loadConstants():
    const = Constants.Constants()
    return const

@pytest.fixture
def client():
    app = Flask(__name__)
    with app.test_client() as client:
        yield client

# @pytest.mark.xfail
# @pytest.mark.skip

def test_home(loadConstants,client):
    url = '/home'
    response = client.get(url)
    assert response == 'homepage'
    
def test_create_shopper(loadConstants,client):
    url = '/createUser/'
    data = getattr(loadConstants,'CREATE_SHOPPER')
    headers = {
        'Content-Type': 'application/json',
    }
    response = client.post(url, data=json.dumps(data), headers=headers)
    assert response.status_code == 200