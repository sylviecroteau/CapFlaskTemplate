from flask_login import UserMixin
from app import login
from mongoengine import EmailField, StringField, IntField, ReferenceField, DateTimeField
from flask_mongoengine import Document
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, Document):
    username = StringField()
    password_hash = StringField()
    fname = StringField()
    lname = StringField()
    email = EmailField()
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login.user_loader
def load_user(id):
    return User.objects.get(pk=id)
