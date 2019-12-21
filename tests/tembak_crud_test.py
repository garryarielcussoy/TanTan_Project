import json
from . import app, client, cache, create_token, db_reset

class TestClientCrud():
    db_reset()
    # Test Case Post 
    def test_client_post_valid(self, client):
        token = create_token(True)

        data = {
            'ip': ''
            'date_birth': '03-05-1996'
            'text':
        }

        res = client.post('/client', query_string = data, headers={'Authorization': 'Bearer ' + token})
        res_json = json.loads(res.data)

        assert res.status_code == 200
        assert res_json['id'] > 0

    # Test Case Put 
    def test_client_put_valid(self, client):
        
        token = create_token(True)

        data = {
            'name': 'user satu',
            'username': 'usersatu',
            'password': 'passusersatu',
            'date_birth': '03-05-1996'
        }

        res = client.put('/client/1', query_string = data, headers={'Authorization': 'Bearer ' + token})
        res_json = json.loads(res.data)
        
        assert res.status_code == 200
        assert res_json['id'] > 0
    
    # Test Case Get All 
    def test_client_get_all_valid(self, client):
        
        token = create_token(True)

        data = {
            'p':1,
            'rp':2
        }

        res = client.get('/client', query_string = data, headers={'Authorization': 'Bearer ' + token})
        res_json = json.loads(res.data)

        assert res.status_code == 200
    
    # Test Case Get by ID 
    def test_client_get_by_id_valid(self, client):
        
        token = create_token(True)

        data = {
            'p':1,
            'rp':2
        }

        res = client.get('/client/1', query_string = data, headers={'Authorization': 'Bearer ' + token})
        res_json = json.loads(res.data)

        assert res.status_code == 200
    
    # Test Case Delete
    def test_client_delete_by_id_valid(self, client):
        
        token = create_token(True)

        data = {
            'p':1,
            'rp':2
        }

        res = client.delete('/client/1', query_string = data, headers={'Authorization': 'Bearer ' + token})
        res_json = json.loads(res.data)

        assert res.status_code == 200

