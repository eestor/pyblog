from flask import Blueprint, render_template, abort, flash, redirect, url_for
from flask_login import login_required, current_user
from ..models.post import Post
from datetime import datetime as dt
from ..models.permission import Permission
from ..models.user import User
from ..forms.edit_profile_form import EditProfileForm
from .. import db

main = Blueprint('main', __name__)


@main.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)


@main.route('/')
@main.route('/home')
@login_required
def home():
    objects = []
    posts = Post.query.order_by(Post.timestamp.desc()).all()
    return render_template('home.html', posts=posts, current_time=dt.utcnow(), object_list=posts)


@main.route('/user/<username>', methods=['GET', 'POST'])
@login_required
def user(username):
    form = EditProfileForm()
    user = User.query.filter_by(username=username).first()
    if user is None:
        abort(404)
    if form.validate_on_submit():
        user.email=form.email.data
        user.username=form.username.data
        user.about_me=form.about_me.data
        user.location=form.location.data
        db.session.commit()
        return redirect(url_for('main.user', username=user.username))
    form.email.data =  user.email
    form.username.data = user.username
    form.location.data = user.location
    form.about_me.data = user.about_me
    return render_template('user.html', user=user, form=form)


