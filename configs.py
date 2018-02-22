import os


def GenerateKey():
    return os.urandom(64)

DB_NAME = 'home_server'

DEV = {
    'CUSTOM_TEST_URL': True,
    'DEBUG': True,
    'JS_TEST': True,
    'SECRET_KEY': 'key',
    'SQLALCHEMY_TRACK_MODIFICATIONS': False,
    'SQLALCHEMY_DATABASE_URI': 'sqlite:///'+DB_NAME+'.db',
    'WTF_CSRF_SECRET_KEY': 'key'
}

DEPLOY = {
    'CUSTOM_TEST_URL': False,
    'DEBUG': False,
    'JS_TEST': False,
    'SECRET_KEY': GenerateKey(),
    'SQLALCHEMY_TRACK_MODIFICATIONS': False,
    'SQLALCHEMY_DATABASE_URI': 'sqlite:///'+DB_NAME+'.db',
    'WTF_CSRF_SECRET_KEY': GenerateKey()
}


def get_conf( c="DEPLOY" ):
    if c == "DEPLOY":
        return DEPLOY
    elif c == "DEV":
        return DEV
    else:
        return DEPLOY