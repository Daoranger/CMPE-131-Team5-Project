from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateTimeField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from datetime import datetime


class LoginForm(FlaskForm):
    username = StringField('Userename', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class CreateAccountForm(FlaskForm):
    name = StringField('Full Name', validators=[DataRequired()])
    email = StringField('Email Address', validators=[DataRequired(), Email()])
    email_confirm = StringField('Confirm Your Email Address', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Choose Password', validators=[DataRequired(), EqualTo('password_confirm', message='Passwords must match')])
    password_confirm = PasswordField('Confirm Password')
    submit = SubmitField('Create Account')

class CreateNoteForm(FlaskForm):
    title = StringField('Note title', validators=[DataRequired()])
    date = DateTimeField('Date', validators=[DataRequired()], default=datetime.now())
    text = TextAreaField('Note', validators=[DataRequired()])
    submit = SubmitField('Create Note', validators=[DataRequired()])

class EditNoteForm(FlaskForm):
    title = StringField('Note title', validators=[DataRequired()])
    date = DateTimeField('Date', validators=[DataRequired()])
    text = TextAreaField('Note', validators=[DataRequired()])
    submit = SubmitField('Edit Note', validators=[DataRequired()])

