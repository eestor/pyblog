from flask import Blueprint, render_template
from flask_login import login_required
from ..models.post import Post
from datetime import datetime as dt

main = Blueprint('main', __name__)


@main.route('/')
@main.route('/home')
@login_required
def home():
    data = {}
    posts = Post.query.all()
    for post in posts:
        data[post.id] = {'id': post.id,
                         'body': post.body,
                         'timestamp': post.timestamp,
                         'author_id': post.author_id
                         }

    return render_template('home.html', posts=data, current_time=dt.utcnow())
