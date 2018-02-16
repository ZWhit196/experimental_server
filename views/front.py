from flask import Blueprint, request, Response, flash, jsonify
from flask.templating import render_template
from flask.helpers import url_for

from helpers import Error, Load_data

front_router = Blueprint('front', __name__, template_folder='templates')

@front_router.route("/", methods=["GET"])
def home():
    return render_template("front/home.html")