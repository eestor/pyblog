from flask import Blueprint, render_template, abort, flash, redirect, url_for, request, current_app
from flask_login import login_required, current_user
from ..models.post import Post
from datetime import datetime as dt
from ..models.permission import Permission
from ..models.user import User
from ..forms.edit_profile_form import EditProfileForm
from ..forms.post_form import PostForm
from .. import db

main = Blueprint('main', __name__)


@main.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)


@main.route('/home')
@main.route('/', methods=['GET', 'POST'])
def home():
    form = PostForm()
    if current_user.can(Permission.WRITE_ARTICLES) and \
        form.validate_on_submit():
        post = Post(body=form.body.data,
                    author=current_user._get_current_object())
        db.session.add(post)
        return redirect(url_for('main.home'))
    #posts = Post.query.order_by(Post.timestamp.desc()).all()
    page = request.args.get('page', 1, type=int)
    pagination = Post.query.order_by(Post.timestamp.desc()).paginate(page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
        error_out=False)
    posts = pagination.items
    return render_template('home.html', form=form, posts=posts, current_time=dt.utcnow(), pagination=pagination)


@main.route('/user/<username>', methods=['GET', 'POST'])
@login_required
def user(username):
    form = EditProfileForm()
    user = User.query.filter_by(username=username).first()
    if user is None:
        abort(404)
    if form.validate_on_submit():
        user.email = form.email.data
        user.username = form.username.data
        user.about_me = form.about_me.data
        user.location = form.location.data
        db.session.commit()
        return redirect(url_for('main.user', username=user.username))
    form.email.data = user.email
    form.username.data = user.username
    form.location.data = user.location
    form.about_me.data = user.about_me
    posts = user.posts.order_by(Post.timestamp.desc()).all()
    return render_template('user.html', user=user, form=form, posts=posts)
