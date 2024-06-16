from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField
from wtforms.validators import email, data_required


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[data_required()])
    email = EmailField('Email', validators=[data_required(), email()])
    password = PasswordField('Password', validators=[data_required()])
    submit = SubmitField('Submit')


class LoginForm(RegistrationForm):
    username = None
