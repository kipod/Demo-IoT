from flask import Blueprint, render_template, url_for, redirect, flash, request
from flask_login import login_user, logout_user, login_required

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
