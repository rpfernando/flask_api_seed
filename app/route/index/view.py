from flask.ext.classy import route
from utils import RouteView, get_json

# API route '/'
class IndexView(RouteView):

    def get(self):
        return "get"

    def post(self):
        return "post"

    def delete(self):
        return "delete"

    def put(self):
        return "put"

    # Defining API routes for Index
    @staticmethod
    def load(app):
        IndexView.register(app, route_base='/')
