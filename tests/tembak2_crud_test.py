import json
from . import app, client, cache, create_token, db_reset

class TestClientCrud():
    def test_tembak_get_valid(self, client):
        db_reset()
        token = create_token(False)

        data = {
            'text': 'horoskop'
        }

        res = client.get('/tembak', query_string = data, headers={'Authorization': 'Bearer ' + token})
        res_json = json.loads(res.data)

        assert res.status_code == 200
    

