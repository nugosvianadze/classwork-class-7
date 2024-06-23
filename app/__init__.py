from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from app.urls import register_blueprints
from app.config import Config
from app.user.models import *
from app.library.models import *
from app.extensions import db, migrate, login_manager
from app.utils import FlaskEnv

from os import environ


def create_app():
    app = Flask(__name__)

    register_config(app)
    register_blueprints(app)
    register_admin(app)
    register_extensions(app)
    # with app.app_context():
    #     from app.extensions import db
    #     # print('deleting')
    #     # db.drop_all()
    #     print('Creating database tables...')
    #     db.create_all()
    #     print('Database tables created.')
    return app


def register_admin(app):
    admin = Admin(app, name='Review Book', template_mode='bootstrap4')
    admin.add_view(ModelView(User, db.session, name='User', endpoint='/users'))
    admin.add_view(ModelView(Book, db.session))
    admin.add_view(ModelView(Review, db.session))


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)


def register_config(app):
    env = {
        FlaskEnv.PRODUCTION.value: Config,
        FlaskEnv.DEVELOPMENT.value: Config,
        FlaskEnv.TESTING.value: Config
    }
    app.config.from_object(env[environ.get('FLASK_ENV')])


application = create_app()
