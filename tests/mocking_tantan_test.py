from unittest import mock
from unittest.mock import patch
import json, os
from . import app, client, cache, create_token, db_reset

class TestMockingTanTan():
    # Mocking Function
    def api_mock(*args, **kwargs):
        class MockResponse:
            def __init__(self, json_data, status_code):
                self.json_data = json_data
                self.status_code = status_code
            
            def json(self):
                return self.json_data
        
        if len(args)>0:
            # IPGeolocation Mocking
            if args[0] == 'https://api.ipgeolocation.io/ipgeo':
                return MockResponse({
                    "latitude": "-6.21462",
                    "longitude": "106.84513",
                }, 200)
            # Zomato Mocking
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
            # Simsimi Mocking
            elif args[0] == 'https://wsapi.simsimi.com/190410/talk':
                return MockResponse({
                    "atext": "Halooooo"
                }, 200)
            # Meetup Mocking
            elif args[0] == 'https://api.meetup.com/find/locations':
                return MockResponse([
                    {"location": "Jakarta"}
                ], 200)
            # Anime Mocking
            elif args[0] == 'https://kitsu.io/api/edge/anime':
                return MockResponse({
                    "data": [
                        {
                            "attributes": {
                                "titles": "Shigatsu wa Kimi no Uso",
                                "posterImage": {
                                    "small": "image.jpg"
                                }
                            },
                            "links": {
                                "self": "https://image.com"
                            },
                            "id": "8403"
                        }
                    ]
                }, 200)
        return MockResponse(None, 404)
    
    # Get Restaurant Test
    @mock.patch('requests.get', side_effect=api_mock)
    def test_get_restaurant(self, test_get_restaurant_mock, client):
        db_reset()
        token = create_token(False)
        res = client.get('/tembak', headers={'Authorization': 'Bearer ' + token}, query_string={"text": "TanTan lapeeeer"})
        
        res_json = json.loads(res.data)
        assert res.status_code == 200
        assert res_json['Daftar Restaurant Terdekat:'][0]['Nama Restaurant'] == "Seoul Yummy"
    
    # Simsimi Test
    @mock.patch('requests.post', side_effect=api_mock)
    def test_get_simsimi(self, test_get_simsimi_mock, client):
        db_reset()
        token = create_token(False)
        res = client.get('/tembak', headers={'Authorization': 'Bearer ' + token}, query_string={"text": "Halo TanTan"})
        
        res_json = json.loads(res.data)
        assert res.status_code == 200
        assert res_json['Pesan dari TanTan'] == "Halooooo"

    # Get Friend Test
    @mock.patch('requests.get', side_effect=api_mock)
    def test_get_friend(self, test_get_friend_mock, client):
        db_reset()
        token = create_token(False)
        res = client.get('/tembak', headers={'Authorization': 'Bearer ' + token}, query_string={"text": "Sendirian"})
        
        res_json = json.loads(res.data)
        assert res.status_code == 200
        assert res_json['Daftar Teman yang Bisa Diajak'][0]['location'] == "Jakarta"
    
    # Get Anime Test
    @mock.patch('requests.get', side_effect=api_mock)
    def test_get_anime(self, test_get_anime_mock, client):
        db_reset()
        token = create_token(False)
        os.environ['ANIME'] = '1'
        res = client.get('/tembak', headers={'Authorization': 'Bearer ' + token}, query_string={"text": "Shigatsu"})
        os.environ['ANIME'] = '0'

        res_json = json.loads(res.data)
        assert res.status_code == 200
        assert res_json["Pesan dari TanTan:"]["Judul"] == 'Shigatsu wa Kimi no Uso'