import os

from flask import Blueprint, request, Response, flash, jsonify, redirect
from flask_login import login_required
from flask.templating import render_template
from flask.helpers import url_for

from file_management.folder import FolderManager
from helpers import Error, Load_data

test_router = Blueprint('test', __name__, template_folder='templates')
SERVABLES = "static/servables/"

@test_router.route("/tests", methods=["GET"])
def home():
    filename = "example"
    url = SERVABLES+"vid/"+filename+'.mp4'
    return render_template("testing.html", url=url)


@test_router.route("/tests/folder")
@login_required
def make_base():
    FM = FolderManager()
    print(FM)
    print(FM.Get_urls())
#     print(FM.Create_personal_base())
    return "<p>Folder manager test</p>"



# @test_router.route("/tests/vid/<filename>")
def get_vid(filename):
    pass
#     url = SERVABLES+"vid/"+filename
#     print(url)
#     
#     def generate_stream(url):
#         with open(url) as vid:
# #             print(vid, dir(vid))
#             for l in vid.readlines():
#                 yield l
#     
#     return Response( generate_stream(url) )