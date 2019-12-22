import json
from . import app, client, cache, create_token, db_reset

class TestAuth():
    # Test Case Create Token 
    def test_get_token_valid_client(self, client):
        db_reset()

        data = {
            "username": "user01",
            "password": "passuser01"
        }

        res = client.get('/token', query_string = data)
        res_json = json.loads(res.data)

        assert res.status_code == 200
    def test_get_token_valid_internal(self, client):
        db_reset()

        data = {
            "username": "internal",
            "password": "tantan"
        }

        res = client.get('/token', query_string = data)
        res_json = json.loads(res.data)

        assert res.status_code == 200

    def test_get_token_valid_internal(self, client):
        db_reset()

        data = {
            "username": "internal",
            "password": "lalala"
        }

        res = client.get('/token', query_string = data)
        res_json = json.loads(res.data)

        assert res.status_code == 400
    
    # Test Case Post Token
    def test_get_token_invalid_userpass(self, client):
        db_reset()

        data = {
            "username": "test_token",
            "password": "test_pass"
        }

        res = client.post('/token', query_string = data)
        res_json = json.loads(res.data)

        assert res.status_code == 500


    def test_post_token_jwt_claims_valid(self, client):
        db_reset()
        token = create_token(True)

        res = client.post('/token',headers={'Authorization': 'Bearer ' + token})
        res_json = json.loads(res.data)

        assert res.status_code == 200
        assert res['username'] == 'internal'

    def test_post_token_jwt_claims_valid(self, client):
        db_reset()
        token = create_token(False)

        res = client.post('/token',headers={'Authorization': 'Bearer ' + token})
        res_json = json.loads(res.data)

        assert res.status_code == 200
