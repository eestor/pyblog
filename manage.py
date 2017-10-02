from main import app, db
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from main.models.role import Role
from main.models.user import User
from main.models.post import Post
from werkzeug.contrib.profiler import ProfilerMiddleware
from flask_admin import Admin
import os

def make_shell_context():
    return dict(app=app, db=db, Role=Role, User=User, Post=Post)

app.config.from_object('main.config.DevelopmentConfig')

from main import admin
#app.wsgi_app = ProfilerMiddleware(app.wsgi_app, restrictions=[30])
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)
manager.add_command("shell", Shell(make_context=make_shell_context))





def initialize_db():
    from datetime import datetime as dt
    user_admin=User(id=1 , email='enriqueesto@yahoo.com', username='enriqueestor', password='secret')
    user_user1=User(id=2 , email='user1@yahoo.com', username='user1', password='secret')
    role_admin = Role(id=1, name='Admin', users=[user_admin])
    role_guest = Role(id=2, name='Guest', users=[user_admin, user_user1])
    post1 = Post(id=1, title='Sample Flask-APShcheduler', body='This is a sample for using API Scheduler', timestamp=dt.utcnow(), author_id=1)
    post2 = Post(id=2, title='Sample Flask-APShcheduler2', body='This is a sample2 for using API Scheduler', timestamp=dt.utcnow(), author_id=1)

    db.session.add(user_admin)
    db.session.add(user_user1)
    db.session.add(role_admin)
    db.session.add(role_guest)
    db.session.add(post1)
    db.session.add(post2)

    db.session.add(user_admin)
    db.session.add(user_user1)
    db.session.add(role_admin)
    db.session.add(role_guest)
    db.session.add(post1)
    db.session.add(post2)

    db.session.commit()

port = os.getenv('VCAP_APP_PORT', '5000')

if __name__ == '__main__':
    #db.drop_all()
    #db.create_all()
    print("db has been initialized")
    #initialize_db()
    #manager.run()
    app.run(host='0.0.0.0', port=int(port))