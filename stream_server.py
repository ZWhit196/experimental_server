import os
import traceback

from flask import Flask, request, jsonify
from flask.templating import render_template
from flask_login import LoginManager

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
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
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
        if request.method == "POST":
            return Get_error(status=ex.code)
        msg = ''
        cd = 0
        if ex.code: 
            cd = ex.code
            msg = ERRORS[cd]
            if cd == 500:
                traceback.print_exc()
        else: 
            cd = 500
            msg = "An error occured."
        return render_template('error.html', err=cd, msg=msg)
    
    for route in Routes():
        app.register_blueprint( route )
    
    app.secret_key = "a"#createNewKey()
    return app

def run_app():
    app = create_app()
    if not os.path.isfile('database.db'):
        setup_database(app)
    app.run(host="0.0.0.0", port=5001, debug=True)

if __name__ == "__main__":
    run_app()