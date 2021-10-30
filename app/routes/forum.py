from flask.helpers import url_for
from app import app, login
from flask import render_template, flash, redirect
from flask_login import current_user
from app.classes.data import Post, Comment
from app.classes.forms import PostForm, CommentForm
from flask_login import login_required
import datetime as dt

@app.route('/post/new', methods=['GET', 'POST'])
@login_required
def postNew():
    form = PostForm()

    if form.validate_on_submit():

        newPost = Post(
            subject = form.subject.data,
            content = form.content.data,
            author = current_user.id,
            modifydate = dt.datetime.utcnow
        )
        newPost.save()

        return redirect(url_for('post',postID=newPost.id))

    return render_template('postform.html',form=form)

@app.route('/post/<postID>')
@login_required
def post(postID):
    post = Post.objects.get(id=postID)
    return render_template('post.html',post=post)

@app.route('/post/list')
@login_required
def postList():
    posts = Post.objects()
    return render_template('posts.html',posts=posts)

@app.route('/post/delete/<postID>')
@login_required
def postDelete(postID):
    deletePost = Post.objects.get(id=postID)
    if current_user == deletePost.author:
        deletePost.delete()
        flash('The Post was deleted.')
    else:
        flash("You can't delete a post you don't own.")
    posts = Post.objects()  
    return render_template('posts.html',posts=posts)

@app.route('/post/edit/<postID>', methods=['GET', 'POST'])
@login_required
def postEdit(postID):
    editPost = Post.objects.get(id=postID)
    if current_user != editPost.author:
        flash("You can't edit a post you don't own.")
        return redirect(url_for('post',postID=postID))
    form = PostForm()
    if form.validate_on_submit():
        editPost.update(
            subject = form.subject.data,
            content = form.content.data,
            modifydate = dt.datetime.utcnow
        )
        return redirect(url_for('post',postID=postID))

    form.subject.data = editPost.subject
    form.content.data = editPost.content

    return render_template('postform.html',form=form)
