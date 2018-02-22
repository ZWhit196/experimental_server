import os
import traceback

from flask import Flask, request, jsonify
from flask.templating import render_template
from flask_login import LoginManager

from configs import get_conf, DB_NAME
from DB import db
from models import User
from views import Routes

ERRORS = {400: "There was an issue with the request.", 403: "Access is denied.", 404: "This page/resource was not found.", 500: "An internal server error occured."}


def createNewKey():
    return os.urandom(64)

def setup_database(app):
    with app.app_context():
        db.create_all()

def create_app():
    app = Flask(__name__)
    
    conf = get_conf()
    for key in conf:
        app.config[key] = conf[key]
    
    db.init_app(app)
    
    # login manager
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'accounts.login'
    # keeps the user in the session
    @login_manager.user_loader
    def load_user(uid):
        return User.query.get(int(uid))
    
    @app.errorhandler(400)
    @app.errorhandler(403)
    @app.errorhandler(404)
    @app.errorhandler(500)
    def error_loading(ex):
        cd = 500
        if ex.code: 
            cd = ex.code
        msg = ERRORS[cd]
        if cd == 500:
            traceback.print_exc()
        if request.method == "POST":
            return Error(msg, status=ex.code)
        return render_template('error.html', err=cd, msg=msg)
    
    for route in Routes(True):
        app.register_blueprint( route )
    
    return app

def run_app():
    app = create_app()
    if not os.path.isfile(DB_NAME+'.db'):
        setup_database(app)
    app.run(host="0.0.0.0", port=5001)

if __name__ == "__main__":
    run_app()