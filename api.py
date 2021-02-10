from flask_restful import Resource, reqparse, abort
from envVariables import api

userEmailParser = reqparse.RequestParser()
userEmailParser.add_argument("email", type=str, help="Email of the user")

userInfoParser = reqparse.RequestParser()
userInfoParser.add_argument("email", type=str, help="Email of the User is required", required=True)
userInfoParser.add_argument("name", type=str, help="Name of the User is required", required=True)
userInfoParser.add_argument("phoneNumber", type=str, help="Phone Number of the User", required=True)
userInfoParser.add_argument("city", type=str, help="City of the User", required=True)
userInfoParser.add_argument("street", type=str, help="Street of the User", required=True)
userInfoParser.add_argument("password", type=str, help="Password of the User", required=True)

loginParser = reqparse.RequestParser()
loginParser.add_argument("email", type=str, help="Email of the User is required", required=True)
loginParser.add_argument("password", type=str, help="Password of the User is required", required=True)


def abort_if_user_doesnt_exist(email):
    abort(404, message="Can't find the user")


def abort_if_user_exists(email):
    abort(409, message="User already exist")


class User(Resource):
    def get(self):
        args = userEmailParser.parse_args()
        email = args["email"]
        abort_if_user_doesnt_exist(args["email"])
        return {"email": email}

    def post(self):
        args = userInfoParser.parse_args()
        abort_if_user_exists(args["email"])
        return args


class Login(Resource):
    def post(self):
        args = loginParser.parse_args()
        email = args["email"]
        return args


api.add_resource(User, "/users")
api.add_resource(Login, "/login")
