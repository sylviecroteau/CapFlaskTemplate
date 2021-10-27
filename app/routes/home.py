from app import app
from flask import Flask, render_template

@app.route('/')
def index():
    print('home')
    return render_template('index.html')
