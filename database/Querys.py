from DB import db
from models import User

def _Create_user(email, password):
    ''' Create a user and commit it to the database. '''
    u = User(email, password) # request.form['marketing_opt_in'], # True
    db.session.add(u)
    db.session.commit()
    return u

def _Find_user(email):
    ''' Find a user by email. '''
    return User.query.filter_by(email=email).first()

def _Check_email_used(email):
    ''' Checks whether an email is used. '''
    if User.query.filter_by(email=email).first():
        return True
    return False

def _Reset_user_password(password, email):
    ''' Reset password. '''
    u = User.query.filter_by(email=email).first()
    if u:
        u.update_password(password)
        return True
    return False