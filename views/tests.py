import os

from flask import Blueprint, request, Response, flash, jsonify
from flask.templating import render_template
from flask.helpers import url_for

from helpers import Error, Load_data

test_router = Blueprint('test', __name__, template_folder='templates')
SERVABLES = "static/servables/"

@test_router.route("/tests", methods=["GET"])
def home():
    url = url_for("test.get_vid", filename="example.mp4")
    return render_template("testing.html", url=url)

@test_router.route("/tests/vid/<filename>")
def get_vid(filename):
    url = SERVABLES+"vid/"+filename
    print(url)
    
    def generate_stream(url):
        with open(url) as vid:
#             print(vid, dir(vid))
            for l in vid.readlines():
                yield l
    
    return Response( generate_stream(url) )