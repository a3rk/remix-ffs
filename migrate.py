from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from funding.factory import create_app
from flask_migrate import Migrate, MigrateCommand
import settings

#setup needed objects
app = create_app()
app.config.from_object(settings)

from funding.orm.orm import base
#setup migrate object
migrate = Migrate(app,base)

from funding.orm.orm import User,Payout,Proposal,Comment
#manger
manager = Manager(app)
manager.add_command('db', MigrateCommand)

#import model

if __name__ == '__main__':
    manager.run()