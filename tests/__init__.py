import pytest, json, logging
from flask import Flask, request

from blueprints import app, db
from blueprints.client.model import Client
from app import cache

# Password Encription
from password_strength import PasswordPolicy
import hashlib

def db_reset():
    db.drop_all()
    db.create_all()

    password_1 = hashlib.md5("passuser01".encode()).hexdigest()
    client = Client('user 01', 'user01', password_1,'03-11-1996','120.188.37.192')
    db.session.add(client)
    db.session.commit()

    # For testing if case
    for i in range(1, 10):
        password_hash = hashlib.md5(("PASSUSER" + str(i)).encode()).hexdigest()
        client = Client('NAMA' + str(i), 'USER' + str(i), password_hash, '03-0' + str(i) + '-1996','120.188.37.192')
        db.session.add(client)
        db.session.commit()
    
    for i in range(10, 13):
        password_hash = hashlib.md5(("PASSUSER" + str(i)).encode()).hexdigest()
        client = Client('NAMA' + str(i), 'USER' + str(i), password_hash, '03-' + str(i) + '-1996','120.188.37.192')
        db.session.add(client)
        db.session.commit()

def call_client(request):
    client = app.test_client()
    return client

@pytest.fixture
def client(request):
    return call_client(request)

def create_token(isInternal, nomor_urut = None):
    # Checking whether internal or not and prepare the data
    if isInternal:
        cachename = "test-internal-token"
        data = {
            'username': 'internal',
            'password': 'tantan'
        }
    elif not isInternal and nomor_urut is None:
        cachename = "test-non-internal-token"
        data = {
            'username': 'user01',
            'password': 'passuser01'
        }
    else:
        cachename = "test-non-internal-spesifik-token" + str(nomor_urut)
        data = {
            'username': 'USER' + str(nomor_urut),
            'password': 'PASSUSER' + str(nomor_urut)
        }

    token = cache.get(cachename)
    if token is None:
        # Do Request
        req = call_client(request)
        res = req.get('/token', query_string = data, content_type='application/json')

        # Store Response
        res_json = json.loads(res.data)

        logging.warning('RESULT : %s', res_json)

        # Assertion
        assert res.status_code == 200

        # Save token into cache
        cache.set(cachename, res_json['token'], timeout = 60)

        # Return, because it is useful for other test
        return res_json['token']
    else:
        return token