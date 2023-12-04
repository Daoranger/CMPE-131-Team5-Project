from flask import render_template, flash, jsonify, redirect, url_for
from .forms import CreateAccountForm, CreateNoteForm, EditNoteForm, LoginForm
from app import myapp_obj
from flask import session
import re
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import timedelta
from app import db


from app.dao import *
from app.models import User

#added by Hoang 
import json

import requests
from authlib.integrations.flask_client import OAuth
from flask import Flask, abort, redirect, render_template, session, url_for
#added by Hoang

@myapp_obj.route("/home")
def home():
    return render_template("home.html", session=session.get("user"),
                           pretty=json.dumps(session.get("user"), indent=4))

@myapp_obj.route("/signin-google")
def googleCallback():
    # fetch access token and id token using authorization code
    token = oauth.myApp.authorize_access_token()

    # google people API - https://developers.google.com/people/api/rest/v1/people/get
    # Google OAuth 2.0 playground - https://developers.google.com/oauthplayground
    # make sure you enable the Google People API in the Google Developers console under "Enabled APIs & services" section

    # fetch user data with access token
    personDataUrl = "https://people.googleapis.com/v1/people/me?personFields=genders,birthdays"
    personData = requests.get(personDataUrl, headers={
        "Authorization": f"Bearer {token['access_token']}"
    }).json()
    token["personData"] = personData
    # set complete user information in the session
    session["user_id"] = token
    return redirect(url_for("home"))


@myapp_obj.route("/google-login")
def googleLogin():
    if "user_id" in session:
        abort(404)
    return oauth.myApp.authorize_redirect(redirect_uri=url_for("googleCallback", _external=True))

###################################################



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
    if 'user_id' in session:
        # User is logged in, get user information
        user_id = session['user_id']
        user = get_user_by_id(user_id)  # Implement this function in DAO
        return render_template('dashboard.html', name=user.username, notes=user.notes) #notes=user.notes
    #If not log in can't acess dashboard
    else:
        flash('You are not logged in', 'error')
        return redirect(url_for('login'))   

@myapp_obj.route("/login", methods=['GET', 'POST'])
def login():
    
    #Check if there is already a user in session
    if 'user_id' in session:
        flash('You are already logged in', 'info')
        return redirect('/dashboard')
        
    form = LoginForm()
    if form.validate_on_submit():
        #flash(f'Here we use flash to HTML with the input {form.username.data} and {form.password.data}')
        found_user = get_user(username=form.username.data) #User.query.filter_by(username=form.username.data).first()
        print(found_user)
        
        #if no account with this username in the database, throw error
        if(found_user == None):
            print("no user found")
            #deal with it here
            flash('Error: No user found with this username', 'error')
        #if username found but correct doesn't match throw incorrent password
        elif (not found_user.check_password(password=form.password.data)):
             print("incorrect password")
             flash('Error: Incorrect password', 'error')
        #if password matched username put the user into session and login and redirect to user dashboard
        else:
            session['user_id'] = found_user.id  #storing the user ID of the found_user in the session under the key 'user_id'
            flash('Successful login!', 'success')
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
                
    #Check if Fullname only contain letters
    if form.name.data and (not isinstance(form.name.data, str) or not re.match("^[A-Za-z]*$", form.name.data)):
        flash('Error: Full name can only contain letters', 'error')
        return render_template('create_account.html', form=form)
        
    #Submit and if valid
    if form.validate_on_submit():
            # Hash the password before storing it
            hashed_password = generate_password_hash(form.password.data)
        
            
            #Check if the username or email already exists
            existing_user = User.query.filter((User.username == form.username.data) | (User.email == form.email.data)).first()
            
            #If username existed or email already taken both conditions return the register page
            if existing_user:
                if existing_user.username == form.username.data:
                    flash('Error: This username is already taken', 'error')
                elif existing_user.email == form.email.data:
                    flash('Error: An account with this email address already exists', 'error')
                return render_template('create_account.html', form=form)
           
           
           #TODO: the checking for unique doesn't work here, we need to migrate the db to new models
            if(create_user(username=form.username.data, password=hashed_password,
                     email=form.email.data)):
                session['user_id'] = get_user(username=form.username.data).id
                flash('User created successfully', 'success')
                return redirect('/dashboard')
            else:
                flash('Error: Unable to create the user. Please try again later!', 'error')
                

    return render_template('create_account.html', form=form)

@myapp_obj.route("/logout")
def logout():
    #Pop the user out of their session, redirect back to login
    session.pop('user_id', None)
    flash('You have been logged out', 'success')
    return redirect(url_for('login'))
#@myapp_obj.route("/createnote", methods = ['GET', 'POST'])
#def createnote():
     
@myapp_obj.route("/createnote", methods = ['GET', 'POST'])
def createnote():
    if 'user_id' not in session:
        flash('please log in before trying to create a note')
        return redirect('/login')
    else:
        print(session['user_id'])
        form = CreateNoteForm()
        print(form.validate_on_submit())
        if form.validate_on_submit():
            print('creating new note')
            create_note(title=form.title.data, date=form.date.data, text=form.text.data)
            return redirect('/dashboard')
        return render_template('create_note.html', form=form)

@myapp_obj.route("/edit/<string:noteid>/", methods =['GET', 'POST'])
def edit_note_route(noteid):
     if 'user_id' not in session:
        flash('please log in before trying to edit a note')
        return redirect('/login')
     else:
        curr_note = Note.query.get(int(noteid))
        form = EditNoteForm(title=curr_note.title, date=curr_note.date, text=curr_note.text)
        if form.validate_on_submit():  
            print('form.title.data:', form.title.data )
            if(edit_note(note_id=noteid, date=form.date.data, title=form.title.data, text=form.text.data)):
                print('edited')
                flash('note sucessfully edited')
                return redirect('/dashboard')
     return render_template('edit_note.html', form=form)

@myapp_obj.route("/delete/<string:noteid>/")
def delete_note_route(noteid):
    print("hello")
    if 'user_id' not in session:
        return jsonify({'success': False, 'message': 'user not logged in'})
    else:
        if(delete_note(noteid)):
            print('note successfully deleted')
            flash('note successfully deleted')
            return jsonify({'success': True})
        else:
            print('error, note not deleted')
            flash('error, note not deleted')
            return jsonify({'success': False})
    
'''
@myapp_obj.route("/members/<string:name>/")
def getMember(name):
    return escape(name)
'''