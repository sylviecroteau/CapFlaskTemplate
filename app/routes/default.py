from app import app
from flask import render_template

# This is for rendering the home page
@app.route('/')
def index():
    return render_template('index.html')

<<<<<<< HEAD
@app.route('/whyaccess')
def whyaccess():
    return render_template('whyaccess.html')

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

=======
<<<<<<< HEAD
@app.route('/whyaccess')
def whyaccess():
    return render_template('whyaccess.html')
=======
@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')
>>>>>>> b09bec5b28a11d63088bcdea510a58f3fa08e303
>>>>>>> d5c83b037b30f2430ebb53173c35e4e610d0a372
