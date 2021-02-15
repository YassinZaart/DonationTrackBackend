from flask_restful import Resource, reqparse, abort, request
from envVariables import api

def abort_if_user_doesnt_exist(email):
    abort(404, message="Can't find the user")


def abort_if_user_exists(email):
    abort(409, message="User already exist")


def abort_if_donee_exists(id):
    abort(409, message="Donee already exist")

class User(Resource):
    def get(self):
        email = request.args["email"]
        return {"email": email}

    def post(self):
        args = request.args
        abort_if_user_exists(args["email"])
        return args


class Login(Resource):
    def post(self):
        args = request.args
        email = args["email"]
        return args


class Donee(Resource):
    def post(self):
        args = request.args
        return 200

    def get(self):
        args =request.args
        return args


class Donation(Resource):
    def post(self):
        args = request.args
        return 200


api.add_resource(User, "/users")
api.add_resource(Login, "/login")
api.add_resource(Donee, "/donees")
api.add_resource(Donation, "/donations")
