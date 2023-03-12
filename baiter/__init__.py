import os

from flask import Flask, render_template
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from baiter.auth import DiscordAuth
from baiter.config import config

db = SQLAlchemy()
discord = DiscordAuth()
login_manager = LoginManager()
login_manager.login_view = 'main'


def create_app():
    conf_var = config[os.getenv('CONFIG_APP')]

    # create the Flask app instance
    app = Flask(__name__)

    # configure app settings and extensions
    app.config.from_object(conf_var)

    # initialize extensions
    db.init_app(app)
    discord.init_app(app)
    login_manager.init_app(app)

    @app.route('/healthz')
    def healthz():
        return 'OK'

    # Blueprints
    from baiter.main import main_bp
    from baiter.victims.routes import victims
    app.register_blueprint(main_bp)
    app.register_blueprint(victims)

    # define error handlers
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404

    with app.app_context():
        db.create_all()

    return app
