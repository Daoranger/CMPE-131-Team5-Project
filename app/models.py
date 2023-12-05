from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), nullable=False, unique = True)
    password = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique = True)
    notes = db.relationship("Note", backref="author", lazy=True)
    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        print(f"Stored hashed password: {self.password}")
        result = check_password_hash(self.password, password)
        print(f"Password check result: {result}")
        print(f"Input password: {password}")
        
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f'<user {self.id}: {self.username}>'
    
    
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable = False)
    title = db.Column(db.String(100))
    text = db.Column(db.Text)