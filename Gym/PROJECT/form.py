from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField , SubmitField
from wtforms.validators import DataRequired , Email ,EqualTo 
from wtforms import ValidationError
from models import User
class Register(FlaskForm):
    email =StringField('Email',validators=[DataRequired(),Email()])
    name = StringField('Name',validators=[DataRequired()])
    password =PasswordField('Password',validators=[DataRequired(),EqualTo('password2')])
    password2 =PasswordField('Repeat Password',validators=[DataRequired()])
    submit = SubmitField('Register!')



def check_email(self,field):
    if User.query.filter_by(email=field.data).first():
        raise ValidationError('Your email is already used')

def check_username(self,field):
    if User.query.filter_by(username=field.data).first():
        raise ValidationError('Username already in use')




