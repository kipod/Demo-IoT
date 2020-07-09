from flask import render_template, Blueprint, send_from_directory

main_blueprint = Blueprint('main', __name__)


@main_blueprint.route('/')
def index():
    return render_template('index.html')


@main_blueprint.route('/api/swagger')
def swagger():
    return send_from_directory('static', 'swagger.yaml')
