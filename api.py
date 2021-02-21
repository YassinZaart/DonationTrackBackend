from flask_restful import Resource, request, marshal_with
from variables import api
import schemas
import db_operations
import states
import resource_fields


class User(Resource):

    @marshal_with(resource_fields.user_resource_fields)
    def get(self):
        args = request.args
        user = db_operations.get_user(args["name"])
        return user


class SignUp(Resource):

    def post(self):
        args = request.args
        schema = schemas.SignUpInfoSchema.load(args)
        state = db_operations.signup(args["email"], args["name"],
                                     args["password"], args["city"],
                                     args["street"], args["phoneNumber"])
        if (state == states.SignupState.NAME_ALREADY_EXIST) \
                or (state == states.SignupState.EMAIL_ALREADY_EXIST):
            message = {'message': 'User already exist'}
            return message, 409

        return 200


class Login(Resource):
    def post(self):
        args = request.args
        schemas.LoginSchema().load(args)
        state = db_operations.login(args["email"], args["password"])
        if state == states.LoginState.INCORRECT_PASSWORD:
            message = {'message': 'Incorrect password'}
            return message, 409
        if state == states.LoginState.USER_NOT_FOUND:
            message = {'message': 'User does not exist'}
            return 404
        return 200


class Donee(Resource):
    def post(self):
        args = request.args
        schemas.DoneeSchema().load(args)
        state = db_operations.insert_donee(args["id"], args["fname"], args["lname"],
                                           args["city"], args["street"], args["phone_number"])
        if state == states.DoneeInsertionState.DONEE_EXISTS:
            message = {'message': 'Donee already exist'}
            return message, 409
        return 200

    @marshal_with(resource_fields.donee_resource_fields)
    def get(self):
        args = request.args
        schemas.DoneeIDSchema.load(args)
        donee = db_operations.get_donee(args["id"])
        if donee is None:
            message = {'message': 'Invalid ID'}
            return 404
        return args


class Donation(Resource):
    def post(self):
        args = request.args
        schemas.DonationSchema.load(args)
        state = db_operations.insert_donation(args["id"], args["name"],
                                              args["date"], args["type"],
                                              args["value"])
        if state == states.DonationInsertionState.USER_DOESNT_EXIST:
            message = {'message': 'Invalid User'}
            return message, 404
        if state == states.DonationInsertionState.DONEE_DOESNT_EXIST:
            message = {'message': 'Invalid Donee'}
            return message, 404
        return 200

    @marshal_with(resource_fields.donation_resource_fields)
    def get(self):
        args = request.args
        donations = db_operations.get_donations_by_user(args["name"])
        return donations


api.add_resource(User, "/users")
api.add_resource(Login, "/login")
api.add_resource(Donee, "/donees")
api.add_resource(Donation, "/donations")
api.add_resource(SignUp, "/signup")
