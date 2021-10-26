from flask import Flask

from application.cab.cab_controller import cab_blueprint
from application.exception_handling import exec_blueprint
from application.location.location_controller import location_blueprint


def create_app():
    app = Flask(__name__)

    app.register_blueprint(cab_blueprint)
    app.register_blueprint(exec_blueprint)
    app.register_blueprint(location_blueprint)
    return app
