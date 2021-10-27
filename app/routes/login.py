from app import app, login
from flask import Flask, render_template, redirect,flash,url_for
from app.classes.data import User
from app.classes.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.objects.get(username=form.username.data)
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        newUser = User(
            username=form.username.data, 
            fname=form.fname.data,
            lname=form.lname.data,
            email=form.email.data)
        newUser.save()
        newUser.set_password(form.password.data)

        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))

    return render_template('register.html', title='Register', form=form)