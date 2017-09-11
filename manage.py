from main import app, db
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from main.models import User, Role

def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)

app.config.from_object('main.config.DevelopmentConfig')
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)
manager.add_command("shell", Shell(make_context=make_shell_context))


if __name__ == '__main__':
    manager.run()
