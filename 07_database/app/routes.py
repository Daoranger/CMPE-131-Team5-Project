from flask import render_template
from flask import redirect
from flask import flash
from .forms import LoginForm
from .forms import CreateAccountForm
from app import myapp_obj
from app.models import User
from app import db
import re 


@myapp_obj.route("/")
@myapp_obj.route("/index.html")
def index():
    name = 'Carlos'
    books = [ {'author': 'authorname1',
                'book':'bookname1'},
             {'author': 'authorname2',
              'book': 'bookname2'}]
    return render_template('hello.html',name=name, books=books)

@myapp_obj.route("/hello")
def hello():
    return "Hello World!"

@myapp_obj.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(f'Here we print to terminal the input {form.username.data} and {form.password.data}')
        flash(f'Here we use flash to HTML with the input {form.username.data} and {form.password.data}')
        found_user = User.query.filter_by(username=form.username.data).first()
        print(found_user)

        return redirect('/')
    return render_template('login.html', form=form)

@myapp_obj.route("/createaccount", methods=['GET', 'POST'])
def createaccount():
    form = CreateAccountForm()
    
    # Check if the entered email addresses matched?
    if form.email.data != form.email_confirm.data:
        flash('Error: Email addresses do not match', 'error')
        return render_template('create_account.html', form=form)
        
    # Check if the entered password matched?
    if form.password.data != form.password_confirm.data:
        flash('Error: Password do not match', 'error')
        return render_template('create_account.html', form=form)
    
    if form.validate_on_submit():
        print('do something')
        print(f'this is the username of the user {form.username.data}')
        print(f'this is the password of the user {form.password.data}')
        u = User(username=form.username.data, password=form.password.data,
                     email=form.email.data)
        db.session.add(u)
        db.session.commit()
        return redirect('/')
        
    return render_template('create_account.html', form=form)

@myapp_obj.route("/members/<string:name>/")
def getMember(name):
    return escape(name)

