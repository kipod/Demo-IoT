from flask import render_template, Blueprint, send_from_directory, g
from app import oidc, okta_client

main_blueprint = Blueprint('main', __name__)


@main_blueprint.route('/')
def index():
    return render_template('index.html')


@main_blueprint.route('/api/swagger')
def swagger():
    return send_from_directory('static', 'swagger.yaml')


@main_blueprint.before_request
def before_request():
    if oidc.user_loggedin:
        g.user = okta_client.get_user(oidc.user_getfield("sub"))
        g.email = oidc.user_getfield('email')
        g.name = oidc.user_getfield('name')
    else:
        g.user = None


@main_blueprint.route("/dashboard")
@oidc.require_login
def dashboard():
    return render_template("dashboard.html")
