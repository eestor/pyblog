from flask import Blueprint, render_template, request, redirect, url_for, flash, abort
from flask_login import login_required, logout_user, login_user, current_user
from .. import db
from ..models.user import User
from ..forms.login_form import LoginForm
from ..forms.user_register_form import RegistrationForm

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.home'))
        flash('Invalid username or password.')
    return render_template('login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.home'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        flash('You can now login.')
        return redirect(url_for('auth.login'))
    return render_template('register.html', form=form)


'''
@auth.before_app_request
def before_request():
    if current_user.is_authenticated:
       current_user.ping()
       if not current_user.confirmed and request.endpoint[:5] != 'auth.':
          return redirect(url_for('auth.unconfirmed'))
'''