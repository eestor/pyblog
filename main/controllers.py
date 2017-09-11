from flask import Blueprint, render_template, abort, request, session, redirect, url_for, flash
from flask_login import login_required, logout_user, login_user
from datetime import datetime as dt
from . import db, app
from .models import Resorts, User, Role
from .forms.login_form import LoginForm
import ccy


main = Blueprint('main', __name__)
resorts = Blueprint('resorts', __name__)
auth = Blueprint('auth', __name__)

@main.route('/')
@main.route('/home')
@login_required
def home():
    data = {}
    resorts = Resorts.query.all()
    for resort in resorts:
        data[resort.id] = { 'name' : resort.name,
                 'price' : resort.price,
                 'category': resort.category
                 }
    print(dt.utcnow())

    return render_template('home.html', resorts=data, current_time = dt.utcnow())


@main.route('/user')
def user():
    return render_template('user.html')


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


@resorts.route('/<id>')
def resort(id):
    data = {}
    resort = Resorts.query.get_or_404(id)
    if not resort:
        abort(404)
    data = { 'name': resort.name,
             'price': resort.price,
             'category': resort.category
             }
    return render_template('resorts.html', resort=data)


@resorts.route('/create', methods=['POST', ])
def create_product():
    name = request.form.get('name')
    price = request.form.get('price')
    category = request.form.get('category')
    resort = Resorts(name, price, category)
    db.session.add(resort)
    db.session.commit()
    return 'Product created.'


# Sample context processor
# to use in html template:
# simply call <h4>{{ full_name(product) }}</h4>

'''
@resorts.context_processor
def some_processor():
    def full_name(product):
        return '{0} / {1}'.format(resorts['category'],
                                  resorts['name'])

    return {'full_name': full_name}
'''


# to use in html template:
# <h4>{{ product|full_name }}</h4>
@resorts.app_template_filter('full_name')
def full_name_filter(resort):
    return '{0} / {1}'.format(resort['name'],
                              resort['category'])


@resorts.app_template_filter('format_currency')
def format_currency_filter(amount):
    currency_code = ccy.countryccy(request.accept_languages.best[-2:])
    return '{0} {1}'.format(currency_code, amount)
