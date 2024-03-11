from flask import Flask
from config import Config

def create_app(config_class = Config):
    # Create app
    app = Flask(__name__)

    # Load config
    app.config.from_object(config_class)

    # register blueprints
    from app.blueprints.basic import basic
    app.register_blueprint(basic)

    return app
