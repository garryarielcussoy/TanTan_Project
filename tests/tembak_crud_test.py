import json
from . import app, client, cache, create_token, db_reset

class TestClientCrud():
    def test_tembak_get_valid(self, client):
        db_reset()
        token = create_token(False)

        data = {
            'text': 'aku lapar'
        }

        res = client.get('/tembak', query_string = data, headers={'Authorization': 'Bearer ' + token})
        res_json = json.loads(res.data)

        assert res.status_code == 200
    
    def test_tembak_get_valid(self, client):
        db_reset()
        token = create_token(False)

        data = {
            'text': 'aku bingung'
        }

        res = client.get('/tembak', query_string = data, headers={'Authorization': 'Bearer ' + token})
        res_json = json.loads(res.data)

        assert res.status_code == 200
    
    def test_tembak_get_valid(self, client):
        db_reset()
        token = create_token(False)

        data = {
            'text': 'horoskop'
        }

        res = client.get('/tembak', query_string = data, headers={'Authorization': 'Bearer ' + token})
        res_json = json.loads(res.data)

        assert res.status_code == 200
    
    def test_tembak_get_valid(self, client):
        db_reset()
        token = create_token(False)

        data = {
            'text': 'aku makan'
        }

        res = client.get('/tembak', query_string = data, headers={'Authorization': 'Bearer ' + token})
        res_json = json.loads(res.data)

        assert res.status_code == 200
    
    

    # # Test Case Put 
    # def test_client_put_valid(self, client):
        
    #     token = create_token(True)

    #     data = {
    #         'name': 'user satu',
    #         'username': 'usersatu',
    #         'password': 'passusersatu',
    #         'date_birth': '03-05-1996'
    #     }

    #     res = client.put('/client/1', query_string = data, headers={'Authorization': 'Bearer ' + token})
    #     res_json = json.loads(res.data)
        
    #     assert res.status_code == 200
    #     assert res_json['id'] > 0
    
    # # Test Case Get All 
    # def test_client_get_all_valid(self, client):
        
    #     token = create_token(True)

    #     data = {
    #         'p':1,
    #         'rp':2
    #     }

    #     res = client.get('/client', query_string = data, headers={'Authorization': 'Bearer ' + token})
    #     res_json = json.loads(res.data)

    #     assert res.status_code == 200
    
    # # Test Case Get by ID 
    # def test_client_get_by_id_valid(self, client):
        
    #     token = create_token(True)

    #     data = {
    #         'p':1,
    #         'rp':2
    #     }

    #     res = client.get('/client/1', query_string = data, headers={'Authorization': 'Bearer ' + token})
    #     res_json = json.loads(res.data)

    #     assert res.status_code == 200
    
    # # Test Case Delete
    # def test_client_delete_by_id_valid(self, client):
        
    #     token = create_token(True)

    #     data = {
    #         'p':1,
    #         'rp':2
    #     }

    #     res = client.delete('/client/1', query_string = data, headers={'Authorization': 'Bearer ' + token})
    #     res_json = json.loads(res.data)

    #     assert res.status_code == 200

