from flask_restful import Resource, reqparse
from app.logger import log
from .user_id import UserID


parser = reqparse.RequestParser()
parser.add_argument("name")
parser.add_argument("email")
parser.add_argument("password")


class SignUp(Resource):
    def post(self):
        args = parser.parse_args()
        log(log.INFO, "sign in data: %s", args)
        return UserID(args.name, args.email).to_dict()
