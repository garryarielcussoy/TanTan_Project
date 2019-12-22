import json
from . import app, client, cache, create_token, db_reset

class TestClientCrud():
    db_reset()

# Test Case Post 
    def test_client_post_valid(self, client):
        token = create_token(True)

        data = {
            'name': 'user 01',
            'username': 'user02',
            'password': 'passuser01',
            'date_birth': '03-05-1996',
            'ip' : '120.188.37.192'
        }

        res = client.post('/client', query_string = data, headers={'Authorization': 'Bearer ' + token})
        res_json = json.loads(res.data)

        assert res.status_code == 200
        assert res_json['id'] > 0
    
    def test_client_post_invalid(self, client):
        token = create_token(False)

        data = {
            'name': 'user 01',
            'username': 'user02',
            'password': 'passuser01',
            'date_birth': '03-05-1996',
            'ip' : '120.188.37.192'
        }

        res = client.post('/client', query_string = data, headers={'Authorization': 'Bearer ' + token})
        res_json = json.loads(res.data)

        assert res.status_code == 403

# Test Case Put 
    def test_client_put_valid(self, client):
        
        token = create_token(True)

        data = {
            'name': 'user satu',
            'username': 'usersatu',
            'password': 'passusersatu',
            'date_birth': '03-03-1996',
            'ip' : '120.188.37.192'
        }

        res = client.put('/client/1', query_string = data, headers={'Authorization': 'Bearer ' + token})
        res_json = json.loads(res.data)
        
        assert res.status_code == 200

    def test_client_put_invalid_password(self, client):
        
        token = create_token(True)

        data = {
            'name': 'user satu',
            'username': 'usersatu',
            'password': 'pass',
            'date_birth': '03-03-1996',
            'ip' : '120.188.37.192'
        }

        res = client.put('/client/1', query_string = data, headers={'Authorization': 'Bearer ' + token})
        res_json = json.loads(res.data)
        
        assert res.status_code == 401

    def test_client_put_invalid_id(self, client):
        token = create_token(True)

        data = {
            'name': 'user satu',
            'username': 'usersatu',
            'password': 'passusersatu',
            'date_birth': '03-03-1996',
            'ip' : '120.188.37.192'
        }

        res = client.put('/client/0', query_string = data, headers={'Authorization': 'Bearer ' + token})
        res_json = json.loads(res.data)
        
        assert res.status_code == 400

    def test_client_put_invalid_id_not_in_db(self, client):
        token = create_token(True)

        data = {
            'name': 'user satu',
            'username': 'usersatu',
            'password': 'passusersatu',
            'date_birth': '03-03-1996',
            'ip' : '120.188.37.192'
        }

        res = client.put('/client/999', query_string = data, headers={'Authorization': 'Bearer ' + token})
        res_json = json.loads(res.data)
        
        assert res.status_code == 404
    
    def test_client_put_invalid_id_string(self, client):
        token = create_token(True)

        data = {
            'name': 'user satu',
            'username': 'usersatu',
            'password': 'passusersatu',
            'date_birth': '03-03-1996',
            'ip' : '120.188.37.192'
        }

        res = client.put('/client/asdf', query_string = data, headers={'Authorization': 'Bearer ' + token})
        res_json = json.loads(res.data)
        
        assert res.status_code == 500
    
# Test Case Get All 
    def test_client_get_all_valid(self, client):
        
        token = create_token(True)

        res = client.get('/client', headers={'Authorization': 'Bearer ' + token})
        res_json = json.loads(res.data)

        assert res.status_code == 200

    def test_client_get_all_valid(self, client):
        token = create_token(True)

        res = client.get('/client', headers={'Authorization': 'Bearer ' + token})
        res_json = json.loads(res.data)

        assert res.status_code == 200
    
# Test Case Get by ID 
    def test_client_get_by_id_valid(self, client):
        
        token = create_token(True)

        res = client.get('/client/1', headers={'Authorization': 'Bearer ' + token})
        res_json = json.loads(res.data)

        assert res.status_code == 200

    def test_client_get_by_id_invalid_string(self, client):
        
        token = create_token(True)

        res = client.get('/client/asdf', headers={'Authorization': 'Bearer ' + token})
        res_json = json.loads(res.data)

        assert res.status_code == 404

    def test_client_get_by_id_invalid_integer(self, client):
        
        token = create_token(True)

        res = client.get('/client/0', headers={'Authorization': 'Bearer ' + token})
        res_json = json.loads(res.data)

        assert res.status_code == 404

    def test_client_get_by_id_invalid_integer(self, client):
        
        token = create_token(True)

        res = client.get('/client/999', headers={'Authorization': 'Bearer ' + token})
        res_json = json.loads(res.data)

        assert res.status_code == 404

# Test Case Delete
    def test_client_delete_by_id_valid(self, client):
        token = create_token(True)

        res = client.delete('/client/1', headers={'Authorization': 'Bearer ' + token})
        res_json = json.loads(res.data)

        assert res.status_code == 200

    def test_client_delete_by_id_invalid_not_in_range(self, client):
        token = create_token(True)

        res = client.delete('/client/999', headers={'Authorization': 'Bearer ' + token})
        res_json = json.loads(res.data)

        assert res.status_code == 404

    def test_client_delete_by_id_invalid_string(self, client):
        token = create_token(True)

        res = client.delete('/client/asdf', headers={'Authorization': 'Bearer ' + token})
        res_json = json.loads(res.data)

        assert res.status_code == 404