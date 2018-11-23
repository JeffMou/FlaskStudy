# -*- coding: UTF-8 -*-
# import Flask Script object
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from jmilkfansblog import models, app

# Init manager object via app object
manager = Manager(app)

# Init migrate object via app and db object
migrate = Migrate(app, models.db)

# Create some new commands
manager.add_command("server", Server())
manager.add_command("db", MigrateCommand)

@manager.shell
def make_shell_context():
    """Create a python CLI.

    return: Default import object
    type: `Dict`
    """
    return dict(app=app,
                db=models.db,
                User=models.User,
                Post=models.Post,
                Comment=models.Comment,
                Tag = models.Tag)

if __name__ == '__main__':
    manager.run()
