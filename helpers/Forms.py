from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators

import database


class Register_Form(FlaskForm):
    username = StringField('Username',[validators.Length(min=3, max=30)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')

    def validate(self):
        # run the normal validators
        rv = FlaskForm.validate(self)
        if not rv:
            return False
        # password validation checks
        if len(self.password.data) < 5: # Too short
            self.password.errors.append("The password must be 5 or more characters long, contain 1 number and 1 letter.")
            return False
        if self.password.data.isalpha(): # Only alpha char
            self.password.errors.append("The password must be 5 or more characters long, contain 1 number and 1 letter.")
            return False
        if self.password.data.isdigit(): # Only numerical
            self.password.errors.append("The password must be 5 or more characters long, contain 1 number and 1 letter.")
            return False
        if database.Username_used(self.username.data): # check if username taken
            self.email.errors.append('Email has already been registered.')
            return False
        return True
    
class Login_Form(FlaskForm):
    username = StringField('Username',[validators.Length(min=3, max=30)])
    password = PasswordField('Password', [
        validators.DataRequired(),
    ])

    def validate(self):
        # run the normal validators
        rv = FlaskForm.validate(self)
        if not rv:
            return False
        # password validation checks
        if len(self.password.data) < 5: # Too short
            self.password.errors.append("The password must be 5 or more characters long, contain 1 number and 1 letter.")
            return False
        if self.password.data.isalpha(): # Only alpha char
            self.password.errors.append("The password must be 5 or more characters long, contain 1 number and 1 letter.")
            return False
        if self.password.data.isdigit(): # Only numerical
            self.password.errors.append("The password must be 5 or more characters long, contain 1 number and 1 letter.")
            return False
        return True