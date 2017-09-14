from flask import Blueprint, render_template
from flask_login import login_required
from ..models.post import Post
from datetime import datetime as dt

main = Blueprint('main', __name__)


@main.route('/')
@main.route('/home')
@login_required
def home():
    objects = []
    posts = Post.query.order_by(Post.timestamp.desc()).all()

    return render_template('home.html', posts=posts, current_time=dt.utcnow(), object_list=posts)
