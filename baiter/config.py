import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY', 'my_secret_key')
    DISCORD_CLIENT_ID = os.getenv('DISCORD_CLIENT_ID')
    DISCORD_SECRET_KEY = os.getenv('DISCORD_SECRET_KEY')


class DevConfig(Config):
    FLASK_DEBUG = True
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///myapp.db'
    HOST = 'localhost'
    HTTP = 'http://'
    SERVING_ADDRESS = HOST
    PORT = 5001
    FULL_URL = f"{HTTP}{HOST}:{PORT}"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///project.db'


class DockerConfig(Config):
    FLASK_DEBUG = True
    # testconfig using docker
    SQLALCHEMY_DATABASE_URI = 'sqlite:///project.db'
    HOST = 'localhost'
    SERVING_ADDRESS = HOST
    HTTP = 'http://'
    PORT = 5001
    FULL_URL = f"{HTTP}{HOST}:{PORT}"


class ProdConfig(Config):
    # testconfig using docker
    FLASK_DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    HOST = os.getenv('HOST')
    SERVING_ADDRESS = '0.0.0.0'
    HTTP = 'https://'
    PORT = 5001
    FULL_URL = f"{HTTP}{HOST}"
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')


config = {
    'dev': DevConfig,
    'docker': DockerConfig,
    'prod': ProdConfig
}
