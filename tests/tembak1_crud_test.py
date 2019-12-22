import json, os
from . import app, client, cache, create_token, db_reset

class TestClientCrud():    
    def test_tembak_get_tanya_anime(self, client):
        db_reset()

        token = create_token(False)

        data = {
            'text': 'mau nonton anime'
        }

        res = client.get('/tembak', query_string = data, headers={'Authorization': 'Bearer ' + token})
        res_json = json.loads(res.data)

        assert res.status_code == 200
    
    def test_tembak_get_anime(self, client):
        db_reset()

        token = create_token(False)

        os.environ['ANIME'] = '1'
        data = {
            'text': 'shigatsu'
        }
        os.environ['ANIME'] = '0'

        res = client.get('/tembak', query_string = data, headers={'Authorization': 'Bearer ' + token})
        res_json = json.loads(res.data)

        assert res.status_code == 200
    
    def test_tembak_if_1(self, client):
        db_reset()
        token = create_token(False, 1)

        data = {
            'text': 'TanTan'
        }

        res = client.get('/tembak', query_string = data, headers={'Authorization': 'Bearer ' + token})
        res_json = json.loads(res.data)

        assert res.status_code == 200
    
    def test_tembak_if_2(self, client):
        # db_reset()
        token = create_token(False, 2)

        data = {
            'text': 'TanTan'
        }

        res = client.get('/tembak', query_string = data, headers={'Authorization': 'Bearer ' + token})
        res_json = json.loads(res.data)

        assert res.status_code == 200
    
    def test_tembak_if_3(self, client):
        # db_reset()
        token = create_token(False, 3)

        data = {
            'text': 'TanTan'
        }

        res = client.get('/tembak', query_string = data, headers={'Authorization': 'Bearer ' + token})
        res_json = json.loads(res.data)

        assert res.status_code == 200
    
    def test_tembak_if_4(self, client):
        # db_reset()
        token = create_token(False, 4)

        data = {
            'text': 'TanTan'
        }

        res = client.get('/tembak', query_string = data, headers={'Authorization': 'Bearer ' + token})
        res_json = json.loads(res.data)

        assert res.status_code == 200
    
    def test_tembak_if_5(self, client):
        # db_reset()
        token = create_token(False, 5)

        data = {
            'text': 'TanTan'
        }

        res = client.get('/tembak', query_string = data, headers={'Authorization': 'Bearer ' + token})
        res_json = json.loads(res.data)

        assert res.status_code == 200
    
    def test_tembak_if_6(self, client):
        # db_reset()
        token = create_token(False, 6)

        data = {
            'text': 'pagi sunshine'
        }

        res = client.get('/tembak', query_string = data, headers={'Authorization': 'Bearer ' + token})
        res_json = json.loads(res.data)

        assert res.status_code == 200

    def test_tembak_if_7(self, client):
        # db_reset()
        token = create_token(False, 7)

        data = {
            'text': 'pagi sunshine'
        }

        res = client.get('/tembak', query_string = data, headers={'Authorization': 'Bearer ' + token})
        res_json = json.loads(res.data)

        assert res.status_code == 200
    
    def test_tembak_if_8(self, client):
        # db_reset()
        token = create_token(False, 8)

        data = {
            'text': 'pagi sunshine'
        }

        res = client.get('/tembak', query_string = data, headers={'Authorization': 'Bearer ' + token})
        res_json = json.loads(res.data)

        assert res.status_code == 200
    
    def test_tembak_if_9(self, client):
        # db_reset()
        token = create_token(False, 9)

        data = {
            'text': 'pagi sunshine'
        }

        res = client.get('/tembak', query_string = data, headers={'Authorization': 'Bearer ' + token})
        res_json = json.loads(res.data)

        assert res.status_code == 200
    
    def test_tembak_if_10(self, client):
        # db_reset()
        token = create_token(False, 10)

        data = {
            'text': 'pagi sunshine'
        }

        res = client.get('/tembak', query_string = data, headers={'Authorization': 'Bearer ' + token})
        res_json = json.loads(res.data)

        assert res.status_code == 200
    
    def test_tembak_if_12(self, client):
        # db_reset()
        token = create_token(False, 12)

        data = {
            'text': 'pagi sunshine'
        }

        res = client.get('/tembak', query_string = data, headers={'Authorization': 'Bearer ' + token})
        res_json = json.loads(res.data)

        assert res.status_code == 200