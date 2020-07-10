from flask import Blueprint, url_for, redirect

from app import oidc

auth_blueprint = Blueprint('auth', __name__)


@auth_blueprint.route('/login')
@oidc.require_login
def login():
    return redirect(url_for("main.dashboard"))


@auth_blueprint.route('/logout')
def logout():
    oidc.logout()
    return redirect(url_for("main.index"))
