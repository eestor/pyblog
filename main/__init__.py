from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_admin import Admin
from flask_pagedown import PageDown
from flask_admin.contrib.sqla import ModelView



app = Flask(__name__)
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
pagedown = PageDown(app)



login_manager = LoginManager()
login_manager.init_app(app)
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


from .controllers.authentication import auth
from .controllers.main import main
from .controllers.posts import posts

from .models.role import Role
from .models.user import User
from .models.post import Post
from .models.comment import Comment

from .errors import page_not_found, internal_server_error

app.register_blueprint(main)
app.register_blueprint(auth)
app.register_blueprint(posts)

admin = Admin(app, 'PyBlog Admin')
admin.add_view(ModelView(Role, db.session))
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Post, db.session))
admin.add_view(ModelView(Comment, db.session))



