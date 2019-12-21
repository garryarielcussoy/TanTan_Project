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
                    [
                        {
                            "Nama Restaurant": "Cork & Screw Country Club",
                            "Lokasi": "Senayan National Golf Club - The Maj Senayan, Jl. Asia Afrika Pintu IX, Senayan, Jakarta",
                            "Pilihan Menu": "European, Grill, Asian",
                            "Jam Buka": "10 AM to 2 AM (Mon-Sat), 10 AM to 1 AM (Sun)",
                            "Rating": "4.2"
                        }
                    ]
                }, 200)
        return MockResponse(None, 404)
    
    # Get IP Test
    @mock.patch('requests.get', side_effect=api_mock_get_ip)
    def test_get_ip(self, test_get_ip_mock, client):
        # Hit Tembak
        token = create_token(False)
        res = client.get('/tembak', headers={'Authorization': 'Bearer ' + token}, args={"text": "TanTan lapeeeer"})
        
        # # Get IP Location
        # res = client.get('https://api.ipgeolocation.io/ipgeo', params={'ip': args['ip'], 'apiKey':'49794d165c0541438235dd9544a7922a'})
        # res_json = json.loads(res.data)
        # assert res.status_code == 200
        # assert res_json['latitude'] == "-6.21462"
        # assert res_json['longitude'] == "106.84513"

        # Get Nearby Restaurant
        # res = client.get(, params={}, headers={'user-key': '652b214e65c6d08ddcd5246fd4f8fd2d'})
        # res_json = json.loads(res.data)
        assert res.status_code == 200
        assert res_json[0]['Nama Restaurant'] == "Cork & Screw Country Club"