from flask.ext.classy import route
from flask import request

from route.user.model import User

from db import db_session
from utils import RouteView, get_json

# API route '/anime'
class UserView(RouteView):

    def get(self):
        l = [ User.to_hash(u) for u in User.query.filter().all() ]
        return get_json(l)

    def post(self, name):
        u = User(name)
        db_session.add(u)
        db_session.commit()
        return "post anime " + get_json(request.form)

    def delete(self):
        return "delete anime"

    def put(self):
        return "put anime"

    # Defining API routes for Index
    @staticmethod
    def load(app):
        UserView.register(app, route_base='/user/')
