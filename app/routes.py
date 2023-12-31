from flask import render_template, flash, jsonify, redirect, url_for
from .forms import CreateAccountForm, CreateNoteForm, EditNoteForm, LoginForm, UploadForm
from app import myapp_obj
from flask import session
import re
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from app import db, mail
from flask import request
from flask_mail import Message


from app.dao import *
from app.models import User

@myapp_obj.route("/")
@myapp_obj.route("/index.html/")
def index():
    return redirect('/dashboard')

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
    if 'user_id' in session:
        flash('Only one account please!', 'info')
        return redirect('/dashboard')
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
    
    # Check if Fullname only contains letters and spaces
    if form.name.data and (not isinstance(form.name.data, str) or not re.match("^[A-Za-z\s]*$", form.name.data)):
        flash('Error: Full name can only contain letters and spaces', 'error')
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
     
@myapp_obj.route("/createnote", methods = ['GET', 'POST'])
def createnote():
    if 'user_id' not in session:
        flash('please log in before trying to create a note')
        return redirect('/login')
    else:
        form = CreateNoteForm()
        file_form = UploadForm()
        if form.validate_on_submit():
            print('creating new note')
            create_note(title=form.title.data, date=form.date.data, text=form.text.data)
            return redirect('/dashboard')
        if file_form.validate_on_submit():
            print("data from file:",(file_form.file.data))
            temp_file = file_form.file.data
            create_note(title=temp_file.filename[0:-3], date=datetime.now(), text=temp_file.read())
            return redirect('/dashboard')
        else:
            print(file_form.errors)
        return render_template('create_note.html', form=form, file_form=file_form)

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
        
@myapp_obj.route("/view/<string:noteid>", methods=['GET', 'POST'])
def view_note(noteid):
    if 'user_id' not in session:
        flash('Please log in before trying to view notes')
        return redirect('/login')
    note = get_note(note_id=noteid)
    if note != None:
        return render_template('view_note.html', note=note)
    
@myapp_obj.route("/edit_profile", methods=['GET', 'POST'])
def edit_profile():
    # Check if the user is logged in
    if 'user_id' not in session:
        flash('Please log in before trying to edit your profile')
        return redirect('/login')

    # Get the current user
    user_id = session['user_id']
    user = get_user_by_id(user_id)  # Implement this function in DAO

    # Handle the form for editing username an<string:name>d password
    if request.method == 'POST':
        # Check if the form is for editing the username
        if 'edit_username' in request.form:
            new_username = request.form['new_username']

            # Check if the new username is valid (you can add additional checks)
            if not new_username:
                flash('Error: Username cannot be empty', 'error')
            else:
                # Update the username in the database
                user.username = new_username
                db.session.commit()
                flash('Username updated successfully!', 'success')
                return redirect('/dashboard')

        # Check if the form is for editing the password
        elif 'edit_password' in request.form:
            new_password = request.form['new_password']

            # Check if the new password is valid (you can add additional checks)
            if not new_password:
                flash('Error: Password cannot be empty', 'error')
            else:
                # Hash the new password and update it in the database
                user.password = generate_password_hash(new_password)
                db.session.commit()
                flash('Password updated successfully!', 'success')
                return redirect('/dashboard')

    # Render the edit profile page with the user's information
    return render_template('edit_profile.html', user=user)
    
@myapp_obj.route("/contact_us", methods=['GET', 'POST'])
def contact_us():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        if not name or not email or not message:
            flash('Error: All fields are required', 'error')
        else:
            try:
                # Send email using Flask-Mail
                subject = 'Contact Form Submission'
                sender = 'your@gmail.com'  # Replace with your Gmail address
                recipients = ['your@gmail.com']  # Replace with the email address where you want to receive messages

                msg = Message(subject, sender=sender, recipients=recipients)
                msg.body = f"Name: {name}\nEmail: {email}\nMessage: {message}"

                mail.send(msg)

                flash('Your message has been sent. We will get back to you soon!', 'success')
            except Exception as e:
                print(f"Error sending email: {e}")
                flash('Error sending email. Please try again later.', 'error')

    return render_template('contact_us.html')

@myapp_obj.route("/search_notes", methods=['GET', 'POST'])
def search_notes():
    if 'user_id' not in session:
        flash('Please log in before trying to search notes')
        return redirect('/login')

    if request.method == 'POST':
        search_term = request.form.get('search_term')
        user_id = session['user_id']

        if search_term:
            # Perform the search based on the title
            search_results = search_notes_by_title(user_id, search_term)

            return render_template('search_results.html', search_term=search_term, results=search_results)

        flash('Error: Please enter a search term', 'error')

    return render_template('search_notes.html')