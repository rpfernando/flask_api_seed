from flask.ext.classy import FlaskView
import json

# This will be used as interface to create routes to the app
class RouteView(FlaskView):
    @staticmethod
    def load(app):
        raise Exception("NotImplementedException")

def get_json(dictionary):
    return json.dumps(dictionary, indent=2, sort_keys=True)
