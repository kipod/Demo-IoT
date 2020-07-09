from flask import request
from flask_restful import Resource, reqparse
from app.logger import log


parser = reqparse.RequestParser()
# parser.add_argument("email")
# parser.add_argument("password")


class AuthorizationCode(Resource):
    def post(self):
        log(log.INFO, 'AUTHORIZATION: POST')
        for key in request.args:
            log(log.INFO, "%s: %s", key, request.args[key])

    def get(self):
        log(log.INFO, 'AUTHORIZATION: GET')
        for key in request.args:
            log(log.INFO, "%s: %s", key, request.args[key])
