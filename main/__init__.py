from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_moment import Moment

app = Flask(__name__)

db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

from .controllers.authentication import auth
from .controllers.main import main
from .controllers.posts import posts

from .errors import page_not_found, internal_server_error

app.register_blueprint(main)
app.register_blueprint(auth)
app.register_blueprint(posts)

db.create_all()
