from flask_login.utils import login_required
from app import app, login
from werkzeug.urls import url_parse 
from flask import render_template, redirect, flash, url_for, request
from app.classes.data import User
from app.classes.forms import LoginForm, RegistrationForm, ProfileForm
from flask_login import current_user, login_user, logout_user

@login.user_loader
def load_user(id):
    return User.objects.get(pk=id)

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
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
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
            email=form.email.data
            )
        newUser.save()
        newUser.set_password(form.password.data)

        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))

    return render_template('register.html', title='Register', form=form)

@app.route('/myprofile/edit', methods=['GET','POST'])
@login_required
def profileEdit():
    form = ProfileForm()
    if form.validate_on_submit():
        currUser = User.objects.get(id=current_user.id)
        currUser.update(
            lname = form.lname.data,
            fname = form.fname.data
        )
        if form.image.data:
            if currUser.image:
                currUser.image.delete()
            currUser.image.put(form.image.data, content_type = 'image/jpeg')
            currUser.save()
        return redirect(url_for('myProfile'))

    form.fname.data = current_user.fname
    form.lname.data = current_user.lname

    return render_template('profileform.html', form=form)

@app.route('/myprofile')
@login_required
def myProfile():
    return render_template('profilemy.html')
