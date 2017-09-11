from main import app, db
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
#from main.models.role import Role
from main.models.user import User, Role
from main.models.post import Post
from werkzeug.contrib.profiler import ProfilerMiddleware

def make_shell_context():
    return dict(app=app, db=db, Role=Role, User=User, Post=Post)

app.config.from_object('main.config.DevelopmentConfig')
app.wsgi_app = ProfilerMiddleware(app.wsgi_app, restrictions=[30])
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)
manager.add_command("shell", Shell(make_context=make_shell_context))


if __name__ == '__main__':
    manager.run()
