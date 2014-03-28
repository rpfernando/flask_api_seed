import os
from db import Base, engine
# Load routes for the app
def load(app):
    routes = os.walk(os.path.dirname(__file__) + '/route').next()[1]

    for route in routes:
        try:
            # import views
            exec "from route.%s.view import %sView" % (route, route.capitalize())
            exec "%sView.load(app)" % (route.capitalize())
            # import models
            try:
                exec "from route.%s.model import %s" % (route, route.capitalize())
            except Exception, e:
                if app.config['DEBUG']:
                    print "%s model doesn't exist or could not be loaded" % (route.capitalize())
        except Exception, e:
            if app.config['DEBUG']:
                print "%s could not be loaded" % (route.capitalize())

    # Database init
    Base.metadata.create_all(bind=engine)
