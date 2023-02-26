import os


class Config(object):
    FLASK_DEBUG = True
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'my_secret_key')
    PORT = 5001
    HOST = 'localhost'
    HTTP = 'http://'
    FULL_URL = f"{HTTP}{HOST}:{PORT}"


class DevConfig(Config):
    FLASK_DEBUG = True
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///myapp.db'

    # Discord auth
    DISCORD_CLIENT_ID = os.getenv('DISCORD_CLIENT_ID')
    DISCORD_SECRET_KEY = os.getenv('DISCORD_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///project.db'


class ProdConfig(Config):
    FLASK_DEBUG = False
    PORT = 5000
    HOST = 'dalaran.bengan.dev'
    HTTP = 'https://'
    FULL_URL = f"{HTTP}{HOST}:{PORT}"
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
