from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from security import authenticate, identity
from user import UserRegister
from item import Items, Itemlist

app = Flask(__name__)
app.secret_key = 'Jose'
api = Api(app)

jwt = JWT(app, authenticate, identity)

items = []


api.add_resource(Items, '/item/<string:name>')
api.add_resource(Itemlist, '/items')
api.add_resource(UserRegister, '/register')
app.run(port=5000, debug=True)
