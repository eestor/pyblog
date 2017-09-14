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
    '''
    for post in posts:
        data[post.id] = {'id': post.id,
                         'title': post.title,
                         'body': post.body,
                         'timestamp': post.timestamp,
                         'username': post.users.username
                         }
    '''
    return render_template('home.html', posts=posts, current_time=dt.utcnow())
