import traceback

from flask import Blueprint, request, Response, flash, jsonify, abort, redirect
from flask_login import login_user, logout_user, current_user, login_required
from flask.templating import render_template
from flask.helpers import url_for

from database import Username_used, New_user, Get_user
import helpers
# import


accounts_router = Blueprint('accounts', __name__, template_folder='templates')


@accounts_router.route("/login", methods=["GET","POST"])
def login():
    form = helpers.Login_form()
    if request.method == 'GET':
        return render_template('accounts/login.html', form=form)
    if form.validate_on_submit(): # Basically the `POST` request
        username = form.username.data.lower()
        password = form.password.data
        registered_user = Get_user(username)
        if registered_user is not None:
            login_user(registered_user, remember=True)
            flash("You are logged in.")
            return redirect(url_for("front.home"))
    flash("Username or password is invalid.")
    return redirect(url_for("accounts.login"))


@accounts_router.route("/logout", methods=["GET","POST"])
def logout():
    logout_user()
    flash("You have been logged out.")
    return redirect(url_for('front.home'))


@accounts_router.route("/create", methods=["GET","POST"])
def create():
    try:
        form = helpers.Reg_form()
        if form.validate_on_submit(): # Basically the `POST` request
            taken = Username_used(form.username.data.lower())
            if not taken:
                user = New_user( form.username.data.lower(), form.password.data )
                login_user(user, remember=True)
                
                # Setup folder and update reg.json
#                 FM.Create_personal_base() # Create your personal folder
                
                flash("User has been created. Welcome!")
                return redirect(url_for("front.home"))
            flash("That username has already been taken.")
            return redirect(url_for("accounts.create"))
        if form.username.errors or form.password.errors:
            for err in form.username.errors:
                flash(err)
            for err in form.password.errors:
                flash(err)
            return redirect(url_for("accounts.create"))
        return render_template("accounts/create.html", form=form)
    except Exception as e:
        traceback.print_exc()
        print("Error in create:",e)
        if request.method == "POST":
            return helpers.Error(error="SERVER", status=500)
        abort(500)