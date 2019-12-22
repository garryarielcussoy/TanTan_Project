import requests
import re
import os
from flask import Blueprint
from flask_restful import Api, reqparse, Resource, marshal
from flask_jwt_extended import jwt_required, get_jwt_claims
from blueprints.client.model import Client

bp_tembak = Blueprint('tembak', __name__)
api = Api(bp_tembak)

class Conversation(Resource):
    geo_location = 'https://api.ipgeolocation.io'
    geo_location_api_key = '49794d165c0541438235dd9544a7922a'
    zomato_host = 'https://developers.zomato.com/api/v2.1/search'
    zomato_api_key = '652b214e65c6d08ddcd5246fd4f8fd2d'
    meetup_host = 'https://api.meetup.com/find/locations'
    horroscope_host = 'http://ohmanda.com/api/horoscope/'
    translate_host = 'https://translate.yandex.net/api/v1.5/tr/translate'
    simisimi_host = 'https://wsapi.simsimi.com/190410/talk'
    anime_host = 'https://kitsu.io/api/edge/anime'

    @jwt_required
    def get(self):
        # Set Environment
        if 'ANIME' not in os.environ:
            os.environ['ANIME'] = '0' 
        
        claims = get_jwt_claims()
        client_target = Client.query.filter_by(username = claims['username']).first()
        args = marshal(client_target, Client.client_fields)

        parser = reqparse.RequestParser()
        parser.add_argument('text', location='args', default=None, required = True)
        args_result = parser.parse_args()

        args['text'] = args_result['text']

        # Checking horroscope
        day = int(args['date_birth'][0:2])
        month = int(args['date_birth'][3:5])
        
        if month == 12:
            astro_sign = 'Sagittarius' if (day < 22) else 'Capricorn'
        elif month == 1:
            astro_sign = 'Capricorn' if (day < 20) else 'Aquarius'
        elif month == 2:
            astro_sign = 'Aquarius' if (day < 19) else 'Pisces'
        elif month == 3:
            astro_sign = 'Pisces' if (day < 21) else 'Aries'
        elif month == 4:
            astro_sign = 'Aries' if (day < 20) else 'Taurus'
        elif month == 5:
            astro_sign = 'Taurus' if (day < 21) else 'Gemini'
        elif month == 6:
            astro_sign = 'Gemini' if (day < 21) else 'Cancer'
        elif month == 7:
            astro_sign = 'Cancer' if (day < 23) else 'Leo'
        elif month == 8:
            astro_sign = 'Leo' if (day < 23) else 'Virgo'
        elif month == 9:
            astro_sign = 'Virgo' if (day < 23) else 'Libra'
        elif month == 10:
            astro_sign = 'Libra' if (day < 23) else 'Scorpio'
        elif month == 11:
            astro_sign = 'Scorpio' if (day < 22) else 'Sagittarius'

        if re.search(r"[Aa]nime*", args['text']):
            first_message = 'Mau nonton anime apa?'
            os.environ['ANIME'] = '1'
            return {'Pesan dari TanTan': first_message}, 200

        elif re.search(r"[Hh][Oo]*[Rr][Oo]*[Ss]+[Kk][Oo]*[Pp]", args['text']):
            hor_result =  requests.get(self.horroscope_host + astro_sign.lower())
            hor_result_json = hor_result.json()
            args['text'] = hor_result_json['horoscope']

            # Translate the Text
            trans_result = requests.get(self.translate_host, params={"key":"trnsl.1.1.20191221T044400Z.e189b861b5121f06.17c821d1d518276b6818ff66b3ea38beaf4b5b59", "text":args['text'], "lang": "id"})
            trans_result = marshal(trans_result, Client.translate_fields)
            args['text'] = trans_result['text']
            return {
                "Pesan dari TanTan": args['text'][82:-22]
            }, 200
        elif re.search(r"[Ll]+[Aa]*[Pp]+[AaEe]*[Rr]+", args['text']) or re.search(r"[Mm][Aa]*[Kk][Aa]*[Nn]+", args['text']):
            # Step - 1 - Check lon lat from ip
            rq = requests.get(self.geo_location + '/ipgeo', params={'ip': args['ip'], 'apiKey': self.geo_location_api_key})
            rq_json = rq.json()
            lat = rq_json['latitude']
            lon = rq_json['longitude']

            # Step - 2 - Get nearby restaurant
            rq = requests.get(self.zomato_host, headers={'user-key': self.zomato_api_key}, params={'lat': lat, 'lon':lon, 'radius': 100000, 'count': 5})
            rq_json = rq.json()

            restaurant_list = []
            for restaurant in rq_json['restaurants']:
                detail_info = {
                    "Nama Restaurant": restaurant['restaurant']['name'],
                    "Lokasi": restaurant['restaurant']['location']['address'],
                    "Pilihan Menu": restaurant['restaurant']['cuisines'],
                    "Jam Buka": restaurant['restaurant']['timings'],
                    "Rating": restaurant['restaurant']['user_rating']['aggregate_rating']
                }
                restaurant_list.append(detail_info)
            return {
                "Pesan dari TanTan": "Laper? Nih TanTan kasi {} restaurant terdekat".format(len(restaurant_list)),
                "Daftar Restaurant Terdekat:" : restaurant_list,
            }, 200

        elif os.environ['ANIME'] == '1':
            os.environ['ANIME'] = '0'
            anime_result = requests.get(self.anime_host, params={"filter[text]": args['text']})
            anime_result_json = anime_result.json()
            anime_title = anime_result_json["data"][0]["attributes"]["titles"]
            anime_link = anime_result_json["data"][0]["links"]["self"]
            anime_id = anime_result_json["data"][0]["id"]
            anime_url = anime_result_json["data"][0]["attributes"]["posterImage"]["small"][-10:]
            # image = requests.get("https://media.kitsu.io/anime/poster_images/" + anime_id + "/small.jpg?")
            show_anime = {
                "Judul": anime_title,
                "Link": anime_link,
            }
            return {"Pesan dari TanTan:": show_anime}, 200

        elif re.search(r"[Ss]endiri([a]*n)?", args['text']) or re.search(r"[Mm][Aa]+[Kk][Aa]+[Nn]+", args['text']):
            # Step - 1 - Check lon lat from ip
            rq = requests.get(self.geo_location + '/ipgeo', params={'ip': args['ip'], 'apiKey': self.geo_location_api_key})
            rq_json = rq.json()
            lat = rq_json['latitude']
            lon = rq_json['longitude']

            # Step - 2 - Finding nearby friends
            nearby_friends = requests.get(self.meetup_host, params={"lat": lat, "lon": lon})
            nearby_friends = nearby_friends.json()

            if len(nearby_friends) >= 3:
                n = 3
            else:
                n = len(nearby_friends)

            return {
                "Pesan dari TanTan": "Jangan sendirian ya mblo. Ada {} orang nih dideketmu yang mungkin bisa diajak ngedate hehe :3".format(n),
                "Daftar Teman yang Bisa Diajak" : nearby_friends[0:n]
            }, 200

        else:
            headers = {
                'Content-Type': 'application/json',
                'x-api-key': 'IcIBgu/dPH1MnaMoHuEbXIaCm8vne3jxJ6zK93zu'
            }
            your_text = {
                "utext": args['text'],
                "lang": "id"
            }
            rq = requests.post(self.simisimi_host, params=your_text, headers=headers)
            rq_json = rq.json()
            reply = rq_json['atext']
            return {"Pesan dari TanTan": reply}, 200

api.add_resource(Conversation, '')