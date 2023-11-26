from flask import render_template
from flask import redirect, url_for
from flask import flash
from .forms import LoginForm
from .forms import CreateAccountForm
from app import myapp_obj
import re #from Python "Regular Expression Operations"


from app import db

from flask_login import UserMixin

from app.dao import *
from app.models import User

@myapp_obj.route("/")
@myapp_obj.route("/index.html/")
def index():
    name = 'Carlos'
    books = [ {'author': 'authorname1',
                'book':'bookname1'},
             {'author': 'authorname2',
              'book': 'bookname2'}]
    return render_template('hello.html',name=name, books=books)

@myapp_obj.route("/hello/")
def hello():
    return "Hello World!"
    
@myapp_obj.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')

@myapp_obj.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    
    if form.validate_on_submit():
        flash(f'Here we use flash to HTML with the input {form.username.data} and {form.password.data}')
        found_user = get_user(username=form.username.data) #User.query.filter_by(username=form.username.data).first()
        print(found_user)
        
        if(found_user == None):
             print("no user found")
             #deal with it here
             flash('Error: No user found with this username', 'error')
        elif not found_user.check_password(password=form.password.data):
             print("incorrect password")
             flash('Error: Incorrect password', 'error')
        else:
            print("successful login!", 'sucess')
            return redirect('/dashboard')
        #print(form.password.data)
        '''
        return/do stuff here
        '''
    return render_template('login.html', form=form)

@myapp_obj.route("/register", methods=['GET', 'POST'])
def createaccount():
    form = CreateAccountForm()
    print(form.validate_on_submit())
        
    #Check if the user entered email addresses matched
    if form.email.data != form.email_confirm.data:
        flash("Error: Email addresses do not match")
        return render_template('create_account.html', form=form)
                        
    #Check if the user entered passwords matched?
    if form.password.data != form.password_confirm.data:
        flash('Error: Password do not match', 'error')
        return render_template('create_account.html', form=form)
                
    # Additional validations
    if form.name.data and (not isinstance(form.name.data, str) or not re.match("^[A-Za-z]*$", form.name.data)):
        flash('Error: Full name can only contain letters', 'error')
        return render_template('create_account.html', form=form)
        
    #Submit and if valid
    if form.validate_on_submit():
            print('do something')
            print(f'this is the username of the user {form.username.data}')
            print(f'this is the password of the user {form.password.data}')
            
            
            #Check if the username or email already exists
            existing_user = User.query.filter((User.username == form.username.data) | (User.email == form.email.data)).first()
            
            #If username existed or email already taken both conditions return the register page
            if existing_user:
                if existing_user.username == form.username.data:
                    flash('Error: This username is already taken', 'error')
                elif existing_user.email == form.email.data:
                    flash('Error: An account with this email address already exists', 'error')
                return render_template('create_account.html', form=form)
           
           #TODO: the checking for unique doesn't work here 
            if(create_user(username=form.username.data, password=form.password.data,
                     email=form.email.data)):
                print('user created')
                #do stuff here
                flash('User created sucessfully')
            else:
                flash('Error: Unable to create the user. Please try again later!', 'error')

    return render_template('create_account.html', form=form)

#@myapp_obj.route("/createnote", methods = ['GET', 'POST'])
#def createnote():
     

'''
@myapp_obj.route("/members/<string:name>/")
def getMember(name):
    return escape(name)
'''

