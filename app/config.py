import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class Config:
    FLASK_ADMIN_SWATCH = 'cerulean'
    FLASK_APP = os.environ.get('FLASK_APP', 'asdasd')
    FLASK_ENV = os.environ.get('FLASK_ENV', 'development')
    FLASK_DEBUG = os.environ.get('FLASK_DEBUG', 1)
    SECRET_KEY = os.environ.get('SECRET_KEY', ';od3p40kd')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI', 'sqlite:///app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
