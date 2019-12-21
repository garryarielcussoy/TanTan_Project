from unittest import mock
from unittest.mock import patch
import json
from . import app, client, cache, create_token, db_reset

class TestMockingTanTan():
    # Mocking Function
    def api_mock_get_ip(*args, **kwargs):
        class MockResponse:
            def __init__(self, json_data, status_code):
                self.json_data = json_data
                self.status_code = status_code
            
            def json(self):
                return self.json_data
        
        if len(args)>0:
            if args[0] == 'https://api.ipgeolocation.io/ipgeo':
                return MockResponse({
                    "latitude": "-6.21462",
                    "longitude": "106.84513",
                }, 200)
            elif args[0] == 'https://developers.zomato.com/api/v2.1/search':
                return MockResponse({
                    "restaurants": [
                        {
                            'restaurant': {
                                'name': 'Seoul Yummy',
                                'location': {
                                    'address': 'Puri Indah Mall, Lantai 2, Jl. Puri Indah Raya, Puri Indah, Jakarta'
                                },
                                'cuisines': 'Korean',
                                'timings': '10 AM to 10 PM',
                                'user_rating': {
                                    'aggregate_rating': '4.6'
                                }
                            }
                        }
                    ]
                }, 200)
        return MockResponse(None, 404)
    
    # Get IP Test
    @mock.patch('requests.get', side_effect=api_mock_get_ip)
    def test_get_ip(self, test_get_ip_mock, client):
        # Hit Tembak
        db_reset()
        token = create_token(False)
        res = client.get('/tembak', headers={'Authorization': 'Bearer ' + token}, query_string={"text": "TanTan lapeeeer"})
        
        # # Get IP Location
        # res = client.get('https://api.ipgeolocation.io/ipgeo', params={'ip': args['ip'], 'apiKey':'49794d165c0541438235dd9544a7922a'})
        # res_json = json.loads(res.data)
        # assert res.status_code == 200
        # assert res_json['latitude'] == "-6.21462"
        # assert res_json['longitude'] == "106.84513"

        # Get Nearby Restaurant
        # res = client.get(, params={}, headers={'user-key': '652b214e65c6d08ddcd5246fd4f8fd2d'})
        res_json = json.loads(res.data)
        assert res.status_code == 200
        assert res_json['Daftar Restaurant Terdekat:'][0]['Nama Restaurant'] == "Seoul Yummy"