import models
from envVariables import db
from states import LoginState, SignupState
import schemas

def login(email, password):
    user = models.UserModel.query.filter_by(email=email).first()
    if user is None:
        return LoginState.USER_NOT_FOUND
    if user.password == password:
        return LoginState.LOGIN_SUCCESSFUL
    else:
        return LoginState.INCORRECT_PASSWORD


def signup(email, name, password, city, street, phone_number):
    user = models.UserModel.query.filter_by(email=email).first()
    if user is not None:
        return SignupState.EMAIL_ALREADY_EXIST

    user = models.UserModel.query.filter_by(name=name).first()
    if user is not None:
        return SignupState.NAME_ALREADY_EXIST

    user = models.UserModel(email=email, name=name, phoneNumber=phone_number,
                            city=city, street=street, password=password, isAdmin=False)
    db.session.add(user)
    db.session.commit()
    return SignupState.SIGNUP_SUCCESSFUL


def get_user(name):
    user = models.UserModel.query.filter_by(street=name).all()
    return user