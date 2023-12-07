from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_mail import Message 
from flask_mail import Mail
#from flask_login import LoginManager

# Create a flask application instance called myapp_obj
myapp_obj = Flask(__name__)
myapp_obj.config['WTF_CSRF_ENABLED'] = False

#login_manager = LoginManager(myapp_obj)

# Get the base directory path of the app
basedir = os.path.abspath(os.path.dirname(__file__))

# Configure the variables for the application, first set the secret key for the secure operations, set database connection url, and disable the sqalchemy track modifications (uses less memory)
myapp_obj.config.from_mapping(
    SECRET_KEY = 'you-will-never-guess',
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db'),
    SQLALCHEMY_TRACK_MODIFICATIONS = False,
    
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USE_TLS=False,
    MAIL_USERNAME='your@gmail.com',  # Replace with your Gmail address
    MAIL_PASSWORD='your_password'    # Replace with your Gmail password or app-specific password

)

db = SQLAlchemy(myapp_obj)
mail = Mail(myapp_obj)

#Create app context for databse operations everything in this block has acess to the app. import the user model and the todo model, then create the database
with myapp_obj.app_context():
    from app.models import User
    from app.todo import Todo
    db.create_all()

# routes package has routes to the other features also handles some errors.
from app import routes