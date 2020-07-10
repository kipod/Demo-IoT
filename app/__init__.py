import os

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from werkzeug.exceptions import HTTPException
from flask_oidc import OpenIDConnect
from okta import UsersClient

# instantiate extensions
login_manager = LoginManager()
db = SQLAlchemy()
oidc = None
okta_client = None

OKTA_AUTH_TOKEN = os.environ.get('OKTA_AUTH_TOKEN', None)
OKTA_ORG_URL = "https://dev-329158.okta.com"


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
    login_manager.init_app(app)

    # Register blueprints.
    from app.views import main_blueprint
    from app.auth.views import auth_blueprint
    from app.docs import SWAGGER_URL, swaggerui_blueprint
    from app.api import api_blueprint

    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint)
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
    app.register_blueprint(api_blueprint, url_prefix='/api/v1')

    # Set up flask login.
    from app.auth.models import User, AnonymousUser

    @login_manager.user_loader
    def get_user(id):
        return User.query.get(int(id))

    login_manager.login_view = 'auth.login'
    login_manager.login_message_category = 'info'
    login_manager.anonymous_user = AnonymousUser

    # Error handlers.
    @app.errorhandler(HTTPException)
    def handle_http_error(exc):
        return render_template('error.html', error=exc), exc.code

    return app
