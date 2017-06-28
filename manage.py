import os
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

import app, db
#from app import app, db

app.config.from_object(os.environ['APP_SETTINGS'])
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommnd)

if __name__ == '__main__':
    manager.run()

    