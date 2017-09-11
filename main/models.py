'''
RESORTS = {
    'ResortsWorld': {
        'name': 'Resorts World Manila',
        'category': 'resorts',
        'price': 2500
    },
    'Boracay': {
        'name': 'Boracay Resort',
        'category': 'resorts',
        'price': 649
    },
    'Palawan': {
        'name': 'Palawan',
        'category': 'resorts',
        'price': 649
    },
    'CoralReefs': {
        'name': 'Bataan Coral Reefs',
        'category': 'resorts',
        'price': 549
    }}
'''

from . import db


class Resorts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    category = db.Column(db.String(255))
    price = db.Column(db.Float)

    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def __repr__(self):
        return '<Resorts %d>' % self.id


from . import login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')


