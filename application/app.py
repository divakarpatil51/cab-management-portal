from flask import Flask

from application.cab.cab_controller import cab_blueprint


def create_app():
    app = Flask(__name__)

    app.register_blueprint(cab_blueprint)
    return app
