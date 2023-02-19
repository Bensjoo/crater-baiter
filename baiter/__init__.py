from flask import Flask, render_template
from baiter.auth import DiscordAuth


discord = DiscordAuth()


def create_app():
    # create the Flask app instance
    app = Flask(__name__)

    # configure app settings and extensions
    app.config.from_object('baiter.config.DevConfig')

    # initialize extensions
    # e.g. db = SQLAlchemy(app)
    discord.init_app(app)

    @app.route('/healthz')
    def healthz():
        return 'OK'

    # Blueprints
    from baiter.main import main_bp
    app.register_blueprint(main_bp)

    # define error handlers
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404

    return app

#https://discord.com/oauth2/authorize?scope=identify&client_id=1072209317777907813&redirect_uri=http%3A%2F%2Flocalhost%3A5001%2Foauth%2Fcallback&response_type=code
