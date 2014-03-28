from flask import Flask
import routes_and_models, error_handlers, db

# Creating instance of the API
app = Flask("MagicAPI")
app.config['DEBUG'] = True

# Load error handlers
error_handlers.load(app)

db.load(app)

# Load routes for the app
routes_and_models.load(app)

if __name__ == "__main__":
    app.run()
