from flask import Blueprint, render_template, abort
from flask_login import login_required
from ..models.post import Post
from datetime import datetime as dt
from ..models.permission import Permission
from ..models.user import User

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


@main.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        abort(404)
    return render_template('user.html', user=user)
