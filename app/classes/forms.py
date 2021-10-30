from flask.app import Flask
from flask_wtf import FlaskForm
from mongoengine.fields import EmailField
import mongoengine.errors
#from wtforms.fields.html5 import URLField, DateField, DateTimeField, EmailField
from wtforms.validators import URL, NumberRange, Email, Optional, InputRequired, ValidationError, DataRequired, EqualTo
from wtforms import PasswordField ,widgets, SelectMultipleField, StringField, SubmitField, validators, TextAreaField, HiddenField, IntegerField, SelectField, FileField, BooleanField
from app.classes.data import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me?')
    submit = SubmitField()

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    fname = StringField('First Name', validators=[DataRequired()])
    lname = StringField('Last Name', validators=[DataRequired()])    
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        try:
            user = User.objects.get(username=username.data)
        except mongoengine.errors.DoesNotExist:
            pass
        else:
            raise ValidationError('Please use a different email address.')

    def validate_email(self, email):
        try:
            user = User.objects.get(email=email.data)
        except mongoengine.errors.DoesNotExist:
            pass
        else:
            raise ValidationError('Please use a different email address.')

class PostForm(FlaskForm):
    subject = StringField('Subject', validators=[DataRequired()])
    content = TextAreaField('Post', validators=[DataRequired()])
    submit = SubmitField('Post')

class CommentForm(FlaskForm):
    content = TextAreaField('Comment', validators=[DataRequired()])
    submit = SubmitField('Comment')