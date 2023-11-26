from app.models import User
from app import db
from sqlalchemy import exc

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
        
def get_user_by_id(user_id):
    try:
        user = User.query.get(int(user_id))
        return user
    except Exception as e:
        print(f"Error getting user by ID: {e}")
        return None
    
#TODO: def create_note(): 
#TODO: def get_note():

