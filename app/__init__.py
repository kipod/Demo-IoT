import os

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import HTTPException
from flask_oidc import OpenIDConnect
from okta import UsersClient

# instantiate extensions
db = SQLAlchemy()
oidc = None
okta_client = None

OKTA_AUTH_TOKEN = os.environ.get('OKTA_AUTH_TOKEN', None)
OKTA_ORG_URL = os.environ.get('OKTA_ORG_URL', None)


def create_app(environment='development'):

    from config import config

    # Instantiate app.
    app = Flask(__name__)

    # Set app config.
    env = os.environ.get('FLASK_ENV', environment)
    app.config.from_object(config[env])
    config[env].configure(app)
    global oidc
    oidc = OpenIDConnect(app)
    global okta_client
    okta_client = UsersClient(OKTA_ORG_URL, OKTA_AUTH_TOKEN)

    # Set up extensions.
    db.init_app(app)

    # Register blueprints.
    from app.views import main_blueprint
    from app.auth.views import auth_blueprint
    from app.docs import SWAGGER_URL, swaggerui_blueprint
    from app.api import api_blueprint

    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint)
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
    app.register_blueprint(api_blueprint, url_prefix='/api/v1')

    # Error handlers.
    @app.errorhandler(HTTPException)
    def handle_http_error(exc):
        return render_template('error.html', error=exc), exc.code

    return app
