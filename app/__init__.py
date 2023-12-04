from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

#added by Hoang 
import json

import requests
from authlib.integrations.flask_client import OAuth
from flask import Flask, abort, redirect, render_template, session, url_for
#added by Hoang

#from flask_login import LoginManager

# Create a flask application instance called myapp_obj
myapp_obj = Flask(__name__)

#Google Authentication - Hoang
appConf = {
    "OAUTH2_CLIENT_ID": "350850602986-fpjop8tum4cifcs22n9i7qk3g95k1ko3.apps.googleusercontent.com",
    "OAUTH2_CLIENT_SECRET": "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",
    "OAUTH2_META_URL": "https://accounts.google.com/.well-known/openid-configuration",
    "FLASK_SECRET": "ALongRandomlyGeneratedString",
    "FLASK_PORT": 5000
}
#Google Authentication - Hoang

#login_manager = LoginManager(myapp_obj)

# Get the base directory path of the app
basedir = os.path.abspath(os.path.dirname(__file__))

# Configure the variables for the application, first set the secret key for the secure operations, set database connection url, and disable the sqalchemy track modifications (uses less memory)
myapp_obj.config.from_mapping(
    SECRET_KEY = 'you-will-never-guess',
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db'),
    SQLALCHEMY_TRACK_MODIFICATIONS = False
)

#Google Authentication - Hoang
oauth = OAuth(myapp_obj)
oauth.register(
    "myApp",
    client_id=appConf.get("350850602986-fpjop8tum4cifcs22n9i7qk3g95k1ko3.apps.googleusercontent.com"),
    client_secret=appConf.get("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"),
    client_kwargs={
        "scope": "openid profile email https://www.googleapis.com/auth/user.birthday.read https://www.googleapis.com/auth/user.gender.read",
        # 'code_challenge_method': 'S256'  # enable PKCE
    },
    server_metadata_url=f'{appConf.get("OAUTH2_META_URL")}',
)
#Google Authentication - Hoang

db = SQLAlchemy(myapp_obj)

#Create app context for databse operations everything in this block has acess to the app. import the user model and the todo model, then create the database
with myapp_obj.app_context():
    from app.models import User
    from app.todo import Todo
    db.create_all()

# routes package has routes to the other features also handles some errors.
from app import routes