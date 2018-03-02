from database.DB import db
from models import User

def _Create_user(username, password):
    ''' Create a user and commit it to the database. '''
    u = User(username, password)
    db.session.add(u)
    db.session.commit()
    return u

def _Find_user(username):
    ''' Find a user by email. '''
    return User.query.filter_by(username=username).first()

def _Check_username_used(username):
    ''' Checks whether an email is used. '''
    if User.query.filter_by(username=username).first():
        return True
    return False

def _Reset_user_password(password, username):
    ''' Reset password. '''
    u = User.query.filter_by(username=username).first()
    if u:
        u.update_password(password)
        return True
    return False