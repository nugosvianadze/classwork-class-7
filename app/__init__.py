from flask import Flask
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
    register_extensions(app)
    return app


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
