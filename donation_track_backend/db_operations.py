from donation_track_backend.variables import db, bcrypt
from donation_track_backend import states, models


def login(email, password) -> states.LoginState:
    user = models.UserModel.query.get(email)
    if user is None:
        return states.LoginState.USER_NOT_FOUND
    if bcrypt.check_password_hash(user.password, password):
        return states.LoginState.LOGIN_SUCCESSFUL
    else:
        return states.LoginState.INCORRECT_PASSWORD


def signup(email, name, password, city, street, phone_number) -> states.SignupState:
    user = models.UserModel.query.get(email)
    pw_hash = bcrypt.generate_password_hash(password).decode('utf-8')
    if user is not None:
        return states.SignupState.EMAIL_ALREADY_EXIST
    user = models.UserModel(email=email, name=name, phone_number=phone_number,
                            city=city, street=street, password=pw_hash, is_admin=False)
    db.session.add(user)
    db.session.commit()
    return states.SignupState.SIGNUP_SUCCESSFUL


def get_user(email) -> models.UserModel:
    user = models.UserModel.query.get(email)
    return user


def get_donee(id) -> models.DoneeModel:
    user = models.DoneeModel.query.get(id)
    return user


def insert_donee(id, fname, lname, city, street, phone_number) -> states.DoneeInsertionState:
    donee = models.DoneeModel.query.get(id)
    if donee is not None:
        return states.DoneeInsertionState.DONEE_EXISTS
    donee = models.DoneeModel(id=id, first_name=fname, last_name=lname, city=city,
                              street=street, phone_number=phone_number)
    db.session.add(donee)
    db.session.commit()
    return states.DoneeInsertionState.INSERTION_SUCCESSFUL


def get_donations_by_donee(id) -> models.DonationModel:
    donations = models.DonationModel.query.filter_by(id=id).all()
    return donations


def get_donations_by_user(name) -> models.DoneeModel:
    donations = models.DonationModel.query.filter_by(name=name).all()
    return donations


def insert_donation(id, name, date_time, type, value) -> states.DonationInsertionState:
    donation = models.UserModel.query.filter_by(id=id).first()
    if donation is None:
        return states.DonationInsertionState.DONEE_DOESNT_EXIST
    donation = models.UserModel.query.filter_by(name=name).first()
    if donation is None:
        return states.DonationInsertionState.USER_DOESNT_EXIST
    donation = models.DoneeModel(id=id, name=name, date=date_time,
                                 type=type, value=value)
    db.session.add(donation)
    db.session.commit()
    return states.DonationInsertionState.INSERTION_SUCCESSFUL
