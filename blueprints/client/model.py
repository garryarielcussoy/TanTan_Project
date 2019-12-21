# Import
from blueprints import db
from flask_restful import fields

# Create Model
class Client(db.Model):
    __tablename__ = 'client'
    client_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(255), nullable = False)
    username = db.Column(db.String(255), nullable = False, unique = True)
    password = db.Column(db.String(255), nullable = False)
    date_birth = db.Column(db.String(10), nullable = False)

    client_fields = {
        'client_id': fields.Integer,
        'name': fields.String,
        'username': fields.String,
        'password': fields.String,
        'string': fields.String
    }

    translate_fields = {
        'text': fields.String
    }

    # jwt_claim_fields = {
    #     'client_key': fields.String,
    # }

    def __init__(self, client_id, name, username, password):
        self.client_id = client_id
        self.name = name
        self.username = username
        self.password = password
        self.date_birth = date_birth

    def __repr__(self):
        return '<Client %r>' % self.client_id