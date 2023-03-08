import os


class Config(object):
    FLASK_DEBUG = True
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'my_secret_key')
    DISCORD_CLIENT_ID = os.getenv('DISCORD_CLIENT_ID')
    DISCORD_SECRET_KEY = os.getenv('DISCORD_SECRET_KEY')


class DevConfig(Config):
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///myapp.db'
    HOST = 'localhost'
    HTTP = 'http://'
    PORT = 5001
    FULL_URL = f"{HTTP}{HOST}:{PORT}"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///project.db'


class DockerConfig(Config):
    # testconfig using docker
    SQLALCHEMY_DATABASE_URI = 'sqlite:///project.db'
    HOST = '0.0.0.0'
    URL = 'localhost'
    HTTP = 'http://'
    PORT = 5001
    FULL_URL = f"{HTTP}{URL}:{PORT}"



class ProdConfig(Config):
    FLASK_DEBUG = False
    PORT = 5000
    HOST = 'dalaran.bengan.dev'
    HTTP = 'https://'
    FULL_URL = f"{HTTP}{HOST}:{PORT}"
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')


config = {
    'dev': DevConfig,
    'docker': DockerConfig,
    'prod': ProdConfig
}
