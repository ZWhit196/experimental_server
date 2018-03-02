import datetime
from passlib.hash import pbkdf2_sha512

from database.DB import db


class User(db.Model):
    uid = db.Column('uid', db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String(256), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    account_created = db.Column(db.DateTime())
    last_login = db.Column(db.DateTime())

    def __init__(self, username, password):
        self.username = username.lower()
        self.set_password(password)
        self.account_created = datetime.datetime.now()
        self.last_login = datetime.datetime.now()

    def __repr__(self):
        return '<User: {}>'.format(self.username)

    # functions for login manager
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.uid)
    # End login manager func.
    
    def commit_self(self):
        db.session.add(self)
        db.session.commit()
    
    def set_password(self, password):
        ''' hashes and salts a new password '''
        self.password = pbkdf2_sha512.encrypt(password, rounds=200000, salt_size=16)

    def verify_password(self, password):
        ''' verifies a password '''
        return pbkdf2_sha512.verify(password, self.password)

    def update_password(self, password):
        ''' sets and saves a password '''
        self.set_password(password)
        self.commit_self()

    def update_login(self):
        ''' updates time since last login '''
        self.last_login = datetime.datetime.now()
        self.commit_self()