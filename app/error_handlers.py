from utils import get_json

def load(app):
    @app.errorhandler(404)
    def route_not_found(error):
        return get_json({'message': 'invalide route'}), 404

    @app.errorhandler(405)
    def method_not_allowed(error):
        return get_json({'message': 'method not alowed'}), 405