from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators

import database


class Register_Form(FlaskForm):
    email = StringField('Email Address',[validators.Length(min=6, max=35)])
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
        if len(self.password.data) < 8: # Too short
            self.password.errors.append("The password must be 8 or more characters long, contain 1 number and 1 letter.")
            return False
        if self.password.data.isalpha(): # Only alpha char
            self.password.errors.append("The password must be 8 or more characters long, contain 1 number and 1 letter.")
            return False
        if self.password.data.isdigit(): # Only numerical
            self.password.errors.append("The password must be 8 or more characters long, contain 1 number and 1 letter.")
            return False
        if database.Email_used(self.email.data): # check if email taken
            self.email.errors.append('Email has already been registered.')
            return False
        return True
    
class Login_Form(FlaskForm):
    email = StringField('Email Address',[validators.Length(min=6, max=35)])
    password = PasswordField('Password', [
        validators.DataRequired(),
    ])

    def validate(self):
        # run the normal validators
        rv = FlaskForm.validate(self)
        if not rv:
            return False
        # password validation checks
        if len(self.password.data) < 8: # Too short
            self.password.errors.append("The password must be 8 or more characters long, contain 1 number and 1 letter.")
            return False
        if self.password.data.isalpha(): # Only alpha char
            self.password.errors.append("The password must be 8 or more characters long, contain 1 number and 1 letter.")
            return False
        if self.password.data.isdigit(): # Only numerical
            self.password.errors.append("The password must be 8 or more characters long, contain 1 number and 1 letter.")
            return False
        return True