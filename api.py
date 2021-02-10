from flask_restful import Resource, reqparse, abort
from envVariables import api

userEmailParser = reqparse.RequestParser()
userEmailParser.add_argument("email", type=str, help="Email of the user")

userInfoParser = reqparse.RequestParser()
userInfoParser.add_argument("email", type=str, help="Email of the User is required", required=True)
userInfoParser.add_argument("name", type=str, help="Name of the User is required", required=True)
userInfoParser.add_argument("phoneNumber", type=str, help="Phone Number of the User is required", required=True)
userInfoParser.add_argument("city", type=str, help="City of the User is required", required=True)
userInfoParser.add_argument("street", type=str, help="Street of the User is required", required=True)
userInfoParser.add_argument("password", type=str, help="Password of the User is required", required=True)

loginParser = reqparse.RequestParser()
loginParser.add_argument("email", type=str, help="Email of the User is required", required=True)
loginParser.add_argument("password", type=str, help="Password of the User is required", required=True)

doneeInfoParser = reqparse.RequestParser()
doneeInfoParser.add_argument("id", type=str, help="ID of the Donee is required", required=True)
doneeInfoParser.add_argument("fName", type=str, help="First Name of the Donee is required", required=True)
doneeInfoParser.add_argument("lName", type=str, help="Last Name of the Donee is required", required=True)
doneeInfoParser.add_argument("phoneNumber", type=str, help="Phone Number of the Donee is required", required=True)
doneeInfoParser.add_argument("city", type=str, help="City of the Donee is required", required=True)
doneeInfoParser.add_argument("street", type=str, help="Street of the Donee is required", required=True)

doneeReqParser = reqparse.RequestParser()
doneeReqParser.add_argument("id", type=str, help="ID of the Donee is required", required=True)

donationParser = reqparse.RequestParser()
donationParser.add_argument("name", type=str, help="Name of the Donor is required", required=True)
donationParser.add_argument("id", type=str, help="ID of the Donee is required", required=True)
donationParser.add_argument("date", type=str, help="Date of the donation is required", required=True)
donationParser.add_argument("type", type=str, help="Type of the donation is required", required=True)
donationParser.add_argument("value", type=int, help="Value of the donation is required", required=True)


def abort_if_user_doesnt_exist(email):
    abort(404, message="Can't find the user")


def abort_if_user_exists(email):
    abort(409, message="User already exist")


def abort_if_donee_exists(id):
    abort(409, message="Donee already exist")


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


class Donee(Resource):
    def post(self):
        args = doneeInfoParser.parse_args()
        return 200

    def get(self):
        args = doneeReqParser.parse_args()
        return args


class Donation(Resource):
    def post(self):
        args = donationParser.parse_args()
        return 200


api.add_resource(User, "/users")
api.add_resource(Login, "/login")
api.add_resource(Donee, "/donees")
api.add_resource(Donation, "/donations")
