from flask_login import UserMixin
from mongoengine import EmailField, StringField, IntField, ReferenceField, DateTimeField, CASCADE
from flask_mongoengine import Document
from werkzeug.security import generate_password_hash, check_password_hash
import datetime as dt

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

class Post(Document):
    author = ReferenceField('User',reverse_delete_rule=CASCADE) 
    subject = StringField()
    content = StringField()
    createdate = DateTimeField(default=dt.datetime.utcnow)
    modifydate = DateTimeField()

    meta = {
        'ordering': ['-createdate']
    }

class Comment(Document):
    author = ReferenceField('User',reverse_delete_rule=CASCADE) 
    post = ReferenceField('Post',reverse_delete_rule=CASCADE)
    # This could be used to allow comments on comments
    # comment = ReferenceField('Comment',reverse_delete_rule=CASCADE)
    content = StringField('Comment')
    createdate = DateTimeField(default=dt.datetime.utcnow)
    modifydate = DateTimeField()

    meta = {
        'ordering': ['-createdate']
    }
