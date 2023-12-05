from app.models import User, Note
from app import db
from sqlalchemy import exc
from flask import session
def get_user(username):
    '''
    parameters: 
        username (string): the username to be queried

    returns: 
        user (Models.User) or None: If there is a user with the username queried then the User object will be returned.
        If not, None will be returned.
    '''
    return(User.query.filter_by(username=username).first())

def create_user(username, password, email):
    '''
    parameters:
        username (string): the username to be added (must be unique)
        password (string): plaintext password for new account (hashing will be done within function)
        email (string): email of new user
    returns:
        boolean: True if write was succesfull, false if otherwise
    throws (IntegrityError): if username and email aren't unique this error is 
    '''
    try:
        new_user = User(username=username, password=password, email=email)
        db.session.add(new_user)
        db.session.commit()
        return True
    except exc.IntegrityError:
        db.session.rollback()
        return False

#Get user id

def get_user_by_id(user_id):
    '''
    parameters: 
        username (int): the user id to be queried

    returns: 
        user_id 
        if can't return user id there is a problem with getting the user ID so throw error
    '''
    try:
        user = User.query.get(int(user_id))
        return user
    except Exception as e:
        print(f"Error getting user by ID: {e}")
        return None

#TODO: def create_note(): 
def create_note(date, title, text):
    try:
        user_id = session['user_id']
        new_note = Note(date=date, title=title, text=text, user_id=user_id)
        db.session.add(new_note)
        db.session.commit()
        return True
    except Exception as E:
        print(E)
        return False
    
def edit_note(note_id, date, title, text):
    try:
        edited_note = Note.query.get(int(note_id))
        if (edited_note != None):
            edited_note.date = date
            edited_note.title = title
            edited_note.text = text
            db.session.commit()
            print('hello, we did it')
            return True 
        else:
            return False
    except Exception as E:
        print(E)
        return False

def delete_note(note_id):
    del_note = Note.query.get(note_id)
    if del_note != None:
        try:
            db.session.delete(del_note)
            db.session.commit()
            return True
        except Exception as E:
            print(E)
            return False
    else:
        print('Note not found')
        return False

def get_note(note_id):
    return Note.query.get(note_id)