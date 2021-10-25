# Every level/folder of a Python application has an __init__.py file. The purpose of this file is to connect the levels
# of the app to each other. 

from flask import Flask
import os


app = Flask(__name__)
app.config["SECRET_KEY"] = os.urandom(20)

from .routes import *
