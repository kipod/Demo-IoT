from flask import Blueprint
from flask_restful import Api
from .registration import SignUp, Login, AuthorizationCode


api_blueprint = Blueprint('api', __name__)
api = Api(api_blueprint)

# Register API Resources
api.add_resource(SignUp, '/signup')
api.add_resource(Login, '/signin')
api.add_resource(AuthorizationCode, '/authorization-code/callback')
